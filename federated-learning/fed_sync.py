import logging
import sys
import time
import threading
from flask import Flask, request

import utils.util
from utils.ModelStore import ModelStore
from utils.CentralStore import NextRoundCount, ShutdownCount
from utils.util import ColoredLogger
from models.Fed import fed_avg, node_summarized_sign_sgd

from utils.Train import Train

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("fed_sync")

# TO BE CHANGED
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED
trainer = Train()
model_store = ModelStore()
next_round = NextRoundCount()
shutdown = ShutdownCount()


# STEP #1
def init():
    trainer.init_urls(fed_listen_port)

    # parse args
    trainer.parse_args()
    logger.setLevel(trainer.args.log_level)

    load_result = trainer.init_dataset()
    if not load_result:
        sys.exit()
    trainer.dataset.init_trojan_attack(trainer.args)

    load_result = trainer.init_model()
    if not load_result:
        sys.exit()

    # finally trained the initial local model, which will be treated as first global model.
    trainer.net_glob.train()
    w = trainer.net_glob.state_dict()
    model_store.update_global_model(w, -1)  # -1 means the initial global model


# STEP #1
def start():
    # get uuid for itself
    body_data = {
        "message": "FetchID",
        "data": {},
        "epochs": 0,
        "is_sync": True
    }
    trainer.post_msg_blockchain(body_data)
    # upload md5 hash to ledger
    body_data = {
        "message": "Start",
        "data": {
            "global_model_hash": model_store.global_model_hash,
            "user_number": trainer.args.num_users,
        },
        "epochs": trainer.args.epochs,
        "is_sync": True
    }
    trainer.post_msg_blockchain(body_data)


# STEP #2
def train():
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

    train_start_time = time.time()
    w_local, w_loss = trainer.train()
    w_local = trainer.poisoning_attack(w_local)
    if trainer.args.sign_sgd:
        w_local = model_store.extract_sign(w_local, trainer.args.sign_sgd_beta)
    trainer.round_train_duration = time.time() - train_start_time

    # send local model to the first node
    w_local_compressed = utils.util.compress_tensor(w_local)
    body_data = {
        "message": "train_ready",
        "w_compressed": w_local_compressed,
    }
    trainer.post_msg_trigger(body_data)

    # send hash of local model to the ledger
    model_md5 = utils.util.generate_md5_hash(w_local)
    body_data = {
        "message": "UploadLocalModel",
        "data": {
            "w": model_md5,
        },
        "uuid": trainer.uuid,
        "epochs": trainer.epoch,
        "is_sync": True
    }
    trainer.post_msg_blockchain(body_data)


# STEP #3
def train_count(w_compressed):
    if model_store.local_models_add_count(utils.util.decompress_tensor(w_compressed), trainer.args.num_users):
        logger.debug("Gathered enough train_ready, aggregate global model and send the download link.")
        # aggregate global model
        if trainer.args.sign_sgd:
            trainer.server_learning_rate_adjust(trainer.epoch)
            w_glob = node_summarized_sign_sgd(model_store.local_models, model_store.global_model,
                                              trainer.args.server_lr, trainer.args.num_users)
        else:
            w_glob = fed_avg(model_store.local_models)
        # reset local models after aggregation
        model_store.local_models_reset()
        # save global model for further download
        model_store.update_global_model(w_glob, trainer.epoch)
        # send the download link and hash of global model to the ledger
        body_data = {
            "message": "UploadGlobalModel",
            "data": {
                "global_model_hash": model_store.global_model_hash,
            },
            "uuid": trainer.uuid,
            "epochs": trainer.epoch,
            "is_sync": True
        }
        logger.debug("aggregate global model finished, send global_model_hash [{}] to blockchain in epoch [{}]."
                     .format(model_store.global_model_hash, trainer.epoch))
        trainer.post_msg_blockchain(body_data)


# STEP #7
def round_finish():
    logger.debug("Received latest global model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # download global model
    body_data = {
        "message": "global_model",
        "epochs": trainer.epoch,
    }
    detail = trainer.post_msg_trigger(body_data)
    global_model_compressed = detail.get("global_model")
    w_glob = utils.util.decompress_tensor(global_model_compressed)
    # load hash of new global model, which is downloaded from the leader
    global_model_hash = utils.util.generate_md5_hash(w_glob)
    logger.debug("Received new global model with hash: " + global_model_hash)

    # update server step
    model_store.calculate_server_step(trainer.dump_model(), w_glob)

    # finally, evaluate the global model
    trainer.load_model(w_glob)
    trainer.evaluate_model_with_log(record_communication_time=True)

    # epochs count down to 0
    trainer.epoch += 1
    if trainer.epoch <= trainer.args.epochs:
        body_data = {
            "message": "next_round_count"
        }
    else:
        logger.info("########## ALL DONE! ##########")
        body_data = {
            "message": "shutdown_python"
        }
    trainer.post_msg_trigger(body_data)


# count the next round requests gathered
def next_round_count():
    if next_round.add_count(trainer.args.num_users):
        # reset counts
        next_round.reset()
        # START NEXT ROUND
        body_data = {
            "message": "PrepareNextRound",
            "data": {},
            "epochs": trainer.epoch,
            "is_sync": True
        }
        trainer.post_msg_blockchain(body_data)


def shutdown_count():
    if shutdown.add_count(trainer.args.num_users):
        # send request to blockchain for shutting down the python
        body_data = {
            "message": "ShutdownPython",
            "data": {},
            "uuid": "",
            "epochs": 0,
            "is_sync": True
        }
        trainer.post_msg_blockchain(body_data)


def download_global_model(epochs):
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
    @app.route("/messages", methods=["GET", "POST"])
    def main_handler():
        # For GET
        if request.method == "GET":
            start()
            response = {
                "status": "yes"
            }
            return response
        # For POST
        else:
            data = request.get_json()
            status = "yes"
            detail = {}
            response = {"status": status, "detail": detail}
            # Then judge message type and process
            message = data.get("message")
            if message == "uuid":
                trainer.uuid = int(data.get("uuid"))
            elif message == "prepare":
                threading.Thread(target=train).start()
            elif message == "global_model_update":
                threading.Thread(target=round_finish).start()
            elif message == "shutdown":
                threading.Thread(target=utils.util.my_exit, args=(trainer.args.exit_sleep, )).start()
            return response

    @app.route("/trigger", methods=["GET", "POST"])
    def trigger_handler():
        # For POST
        if request.method == "POST":
            data = request.get_json()
            status = "yes"
            detail = {}
            message = data.get("message")

            if message == "train_ready":
                threading.Thread(target=train_count, args=(data.get("w_compressed"), )).start()
            elif message == "global_model":
                detail = download_global_model(data.get("epochs"))
            elif message == "next_round_count":
                threading.Thread(target=next_round_count).start()
            elif message == "shutdown_python":
                threading.Thread(target=shutdown_count, args=()).start()
            response = {"status": status, "detail": detail}
            return response

    @app.route("/test", methods=["GET", "POST"])
    def test():
        # For GET
        if request.method == "GET":
            test_body = {
                "test": "success"
            }
            return test_body
        # For POST
        else:
            doc = request.get_json()
            return doc


if __name__ == "__main__":
    init()
    flask_app = Flask(__name__)
    my_route(flask_app)
    logger.info("start serving at " + str(fed_listen_port) + "...")
    flask_app.run(host="0.0.0.0", port=fed_listen_port)
