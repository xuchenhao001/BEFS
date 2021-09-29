import logging
import os
import sys
import time
import threading
from flask import Flask, request

import utils
from utils.CentralStore import IPCount
from utils.ModelStore import ModelStore
from utils.Train import Train
from utils.util import dataset_loader, ColoredLogger

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("local_train")

# TO BE CHANGED
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED

# NOT TO TOUCH VARIABLES BELOW
trainer = Train()
model_store = ModelStore()
ipCount = IPCount()


# init: loads the dataset and global model
def init():
    # parse network.config and read the peer addresses
    real_path = os.path.dirname(os.path.realpath(__file__))
    peer_address_list = utils.util.env_from_sourcing(os.path.join(real_path, "../fabric-network/network.config"),
                                                     "PeerAddress").split(" ")
    peer_header_addr = peer_address_list[0].split(":")[0]
    # initially the blockchain communicate server is load on the first peer
    trainer.blockchain_server_url = "http://" + peer_header_addr + ":3000/invoke/mychannel/fabcar"
    # initially the trigger url is load on the first peer
    trainer.trigger_url = "http://" + peer_header_addr + ":" + str(fed_listen_port) + "/trigger"

    # parse args
    trainer.parse_args(len(peer_address_list))
    logger.setLevel(trainer.args.log_level)

    load_result = trainer.init_dataset()
    if not load_result:
        sys.exit()

    load_result = trainer.init_model()
    if not load_result:
        sys.exit()

    # finally trained the initial local model, which will be treated as first global model.
    trainer.net_glob.train()


def train():
    if trainer.uuid == -1:
        trainer.uuid = fetch_uuid()

    # training for all epochs
    while trainer.epoch > 0:
        logger.info("Epoch [{}] train for user [{}]".format(trainer.epoch, trainer.uuid))
        trainer.round_start_time = time.time()
        # calculate initial model accuracy, record it as the bench mark.
        if trainer.is_first_epoch():
            trainer.init_time = time.time()
            trainer.evaluate_model_with_log(record_epoch=0, clean=True)

        train_start_time = time.time()
        w_local = trainer.train()
        w_local = trainer.poisoning_attack(w_local)
        trainer.round_train_duration = time.time() - train_start_time

        # finally, evaluate the global model
        trainer.load_model(w_local)
        trainer.evaluate_model_with_log(record_communication_time=True)

        trainer.epoch -= 1

    logger.info("########## ALL DONE! ##########")
    from_ip = utils.util.get_ip(trainer.args.test_ip_addr)
    body_data = {
        "message": "shutdown_python",
        "uuid": trainer.uuid,
        "from_ip": from_ip,
    }
    trainer.post_msg_trigger(body_data)


def start_train():
    time.sleep(trainer.args.start_sleep)
    train()


def load_uuid():
    new_id = ipCount.get_new_id()
    detail = {"uuid": new_id}
    return detail


def fetch_uuid():
    body_data = {
        "message": "fetch_uuid",
    }
    detail = trainer.post_msg_trigger(body_data)
    uuid = detail.get("uuid")
    return uuid


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
