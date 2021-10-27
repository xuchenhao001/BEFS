import logging
import sys
import time
import threading
from flask import Flask, request

import utils.util
from utils.CentralStore import IPCount
from utils.ModelStore import ModelStore
from utils.Train import Train
from utils.util import ColoredLogger
from models.Fed import FedAvg, signSGD

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("fed_avg")

# TO BE CHANGED
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED

# NOT TO TOUCH VARIABLES BELOW
trainer = Train()
model_store = ModelStore()
ipCount = IPCount()


def init():
    trainer.init_urls(fed_listen_port)

    # parse args
    trainer.parse_args()
    logger.setLevel(trainer.args.log_level)

    load_result = trainer.init_dataset()
    if not load_result:
        sys.exit()

    load_result = trainer.init_model()
    if not load_result:
        sys.exit()

    # finally trained the initial local model, which will be treated as first global model.
    trainer.net_glob.train()
    # generate md5 hash from model, which is treated as global model of previous round.
    w = trainer.net_glob.state_dict()
    model_store.update_global_model(w, -1)  # -1 means the initial global model


def train():
    if trainer.uuid == -1:
        trainer.uuid = fetch_uuid()
    logger.debug("Train local model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    trainer.round_start_time = time.time()
    # calculate initial model accuracy, record it as the bench mark.
    if trainer.is_first_epoch():
        trainer.init_time = time.time()
        # download initial global model
        body_data = {
            "message": "global_model",
            "epochs": -1,
        }
        detail = trainer.post_msg_trigger(body_data)
        global_model_compressed = detail.get("global_model")
        w_glob = utils.util.decompress_tensor(global_model_compressed)
        trainer.load_model(w_glob)
        trainer.evaluate_model_with_log(record_epoch=0, clean=True)
    else:
        trainer.load_model(model_store.global_model)

    train_start_time = time.time()
    w_local, w_loss = trainer.train()
    w_local = trainer.poisoning_attack(w_local)
    if trainer.args.sign_sgd:
        w_local = model_store.extract_sign(w_local, trainer.args.sign_sgd_beta)
    trainer.round_train_duration = time.time() - train_start_time

    # send local model to the first node
    w_local_compressed = utils.util.compress_tensor(w_local)
    from_ip = utils.util.get_ip(trainer.args.test_ip_addr)
    body_data = {
        "message": "upload_local_w",
        "w_compressed": w_local_compressed,
        "uuid": trainer.uuid,
        "from_ip": from_ip,
    }
    trainer.post_msg_trigger(body_data)


def start_train():
    time.sleep(trainer.args.start_sleep)
    train()


def gathered_global_w(w_glob_compressed):
    logger.debug("Received latest global model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # load hash of new global model, which is downloaded from the leader
    w_glob = utils.util.decompress_tensor(w_glob_compressed)

    # update server step
    model_store.calculate_server_step(trainer.dump_model(), w_glob)

    # finally, evaluate the global model
    trainer.load_model(w_glob)
    trainer.evaluate_model_with_log(record_communication_time=True)

    # epochs count down to 0
    trainer.epoch += 1
    if trainer.epoch <= trainer.args.epochs:
        train()
    else:
        logger.info("########## ALL DONE! ##########")
        from_ip = utils.util.get_ip(trainer.args.test_ip_addr)
        body_data = {
            "message": "shutdown_python",
            "uuid": trainer.uuid,
            "from_ip": from_ip,
        }
        trainer.post_msg_trigger(body_data)


def average_local_w(uuid, from_ip, w_compressed):
    ipCount.set_map(uuid, from_ip)
    if model_store.local_models_add_count(utils.util.decompress_tensor(w_compressed), trainer.args.num_users):
        logger.debug("Gathered enough w, average and release them")
        if trainer.args.sign_sgd:
            trainer.server_learning_rate_adjust(trainer.epoch)
            w_glob = signSGD(model_store.local_models, model_store.global_model, trainer.args.server_lr,
                             trainer.args.num_users)
        else:
            w_glob = FedAvg(model_store.local_models)
        # reset local models after aggregation
        model_store.local_models_reset()
        # save global model
        model_store.update_global_model(w_glob, trainer.epoch)
        for uuid in ipCount.get_keys():
            body_data = {
                "message": "release_global_w",
                "w_compressed": model_store.global_model_compressed,
            }
            my_url = "http://" + ipCount.get_map(uuid) + ":" + str(fed_listen_port) + "/trigger"
            utils.util.http_client_post(my_url, body_data)


def fetch_uuid():
    body_data = {
        "message": "fetch_uuid",
    }
    detail = trainer.post_msg_trigger(body_data)
    uuid = detail.get("uuid")
    return uuid


def load_uuid():
    new_id = ipCount.get_new_id()
    detail = {"uuid": new_id}
    return detail


def load_global_model(epochs):
    if epochs == model_store.global_model_version:
        detail = {
            "global_model": model_store.global_model_compressed,
        }
    else:
        detail = {
            "global_model": None,
        }
    return detail


def my_route(app):
    @app.route("/trigger", methods=["GET", "POST"])
    def trigger_handler():
        # For POST
        if request.method == "POST":
            data = request.get_json()
            status = "yes"
            detail = {}
            message = data.get("message")
            if message == "fetch_uuid":
                detail = load_uuid()
            elif message == "global_model":
                detail = load_global_model(data.get("epochs"))
            elif message == "upload_local_w":
                threading.Thread(target=average_local_w, args=(
                    data.get("uuid"), data.get("from_ip"), data.get("w_compressed"))).start()
            elif message == "release_global_w":
                threading.Thread(target=gathered_global_w, args=(data.get("w_compressed"), )).start()
            elif message == "shutdown_python":
                threading.Thread(target=utils.util.shutdown_count, args=(
                    data.get("uuid"), data.get("from_ip"), fed_listen_port, trainer.args.num_users)).start()
            elif message == "shutdown":
                threading.Thread(target=utils.util.my_exit, args=(trainer.args.exit_sleep, )).start()
            response = {"status": status, "detail": detail}
            return response


def main():
    # init dataset and global model
    init()

    threading.Thread(target=start_train, args=()).start()

    flask_app = Flask(__name__)
    my_route(flask_app)
    logger.info("start serving at " + str(fed_listen_port) + "...")
    flask_app.run(host="0.0.0.0", port=fed_listen_port)


if __name__ == "__main__":
    main()
