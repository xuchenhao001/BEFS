import logging
import random
import sys
import time
import threading
from flask import Flask, request

import utils.util
from utils.CentralStore import ShutdownCount
from utils.ModelStore import AsyncModelStore
from utils.Train import Train
from utils.util import ColoredLogger
from models.Fed import FadeFedAvg

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("fed_async")

# TO BE CHANGED
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED
trainer = Train()
model_store = AsyncModelStore()
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
        "is_sync": False
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
        "is_sync": False
    }
    trainer.post_msg_blockchain(body_data)


# STEP #2
def train():
    logger.debug("Train local model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    trainer.round_start_time = time.time()
    if trainer.is_first_epoch():
        trainer.init_time = time.time()
        # download initial global model
        body_data = {
            "message": "global_model",
        }
        detail = trainer.post_msg_trigger(body_data)
        global_model_compressed = detail.get("global_model")
        w_glob = utils.util.decompress_tensor(global_model_compressed)
        trainer.load_model(w_glob)
        trainer.evaluate_model_with_log(record_epoch=0, clean=True)

    train_start_time = time.time()
    w_local = trainer.train()
    w_local = trainer.poisoning_attack(w_local)
    trainer.round_train_duration = time.time() - train_start_time

    # send local model to the first node for aggregation
    w_local_compressed = utils.util.compress_tensor(w_local)
    body_data = {
        "message": "train_ready",
        "w_compressed": w_local_compressed
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

    # finished aggregate global model, continue next round
    round_finish()


# STEP #3
def aggregate(w_compressed):
    logger.debug("Received a train_ready.")
    # mimic DDoS attacks here
    if trainer.args.ddos_duration == 0 or trainer.args.ddos_duration > model_store.global_model_version:
        logger.debug("Mimic the aggregator under DDoS attacks!")
        if random.random() < trainer.args.ddos_no_response_percent:
            logger.debug("Unfortunately, the aggregator does not response to the local update gradients")
            model_store.version_update()
            return

    logger.debug("Aggregate global model after received a new local model.")
    w_local = utils.util.decompress_tensor(w_compressed)
    # aggregate global model
    fade_c = calculate_fade_c(w_local)
    w_glob = FadeFedAvg(model_store.global_model, w_local, fade_c)
    # test new global model acc and record onto the log
    trainer.load_model(w_glob)
    acc_local, _, _, _, _ = trainer.evaluate_model_with_log(record_epoch=0)
    # update the global model accuracy
    model_store.global_model_acc = acc_local
    # save global model for further download
    model_store.update_global_model(w_glob)
    logger.debug("As a committee leader, calculate new global model hash: " + model_store.global_model_hash)
    # send the download link and hash of global model to the ledger
    body_data = {
        "message": "UploadGlobalModel",
        "data": {
            "global_model_hash": model_store.global_model_hash,
        },
        "uuid": trainer.uuid,
        "epochs": trainer.epoch,
        "is_sync": False
    }
    trainer.post_msg_blockchain(body_data)


def calculate_fade_c(w_local):
    if trainer.args.fade == -1:  # -1 means fade dynamic setting
        logger.debug("fade=-1, dynamic fade setting is adopted!")
        # dynamic fade setting, test new acc_local first
        trainer.load_model(w_local)
        acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4 = trainer.evaluate_model()
        logger.debug("new local model acc: {}, global model acc: {}".format(acc_local, model_store.global_model_acc))
        if trainer.args.model == "lstm":
            # for lstm, acc_local means the mse loss instead of accuracy, the less the better
            if model_store.global_model_acc == -1:
                fade_c = 10
            else:
                try:
                    fade_c = model_store.global_model_acc / acc_local
                except ZeroDivisionError as err:
                    logger.debug("Divided by zero: {}, set scaling factor to 10 by default.".format(err))
                    fade_c = 10
        else:
            # for cnn or mlp models, accuracy the higher the better.
            if model_store.global_model_acc == -1:
                fade_c = 10
            else:
                try:
                    fade_c = acc_local / model_store.global_model_acc
                except ZeroDivisionError as err:
                    logger.debug("Divided by zero: {}, set scaling factor to 10 by default.".format(err))
                    fade_c = 10
        # filter out poisoning local updated gradients whose test accuracy is less than acc_detect_threshold
        if fade_c < trainer.args.poisoning_detect_threshold:
            fade_c = 0
    else:
        logger.debug("fade={}, static fade setting is adopted!".format(trainer.args.fade))
        # static fade setting
        fade_c = trainer.args.fade
    logger.debug("calculated fade_c: {}".format(fade_c))
    return fade_c


# STEP #7
def round_finish():
    logger.debug("Download latest global model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # download global model
    body_data = {
        "message": "global_model",
    }
    detail = trainer.post_msg_trigger(body_data)
    global_model_compressed = detail.get("global_model")
    global_model_version = detail.get("version")
    logger.debug("Successfully fetched global model version: {}".format(global_model_version))
    w_glob = utils.util.decompress_tensor(global_model_compressed)

    # finally, evaluate the global model
    trainer.load_model(w_glob)
    trainer.evaluate_model_with_log(record_communication_time=True)

    # epochs count down until 0
    trainer.epoch -= 1
    if trainer.epoch > 0:
        # start next round of train right now
        train()
    else:
        logger.info("########## ALL DONE! ##########")
        body_data = {
            "message": "shutdown_python"
        }
        trainer.post_msg_trigger(body_data)


def shutdown_count():
    if shutdown.add_count(trainer.args.num_users):
        # send request to blockchain for shutting down the python
        body_data = {
            "message": "ShutdownPython",
            "data": {},
            "uuid": "",
            "epochs": 0,
            "is_sync": False
        }
        trainer.post_msg_blockchain(body_data)


def download_global_model():
    detail = {
        "global_model": model_store.global_model_compressed,
        "version": model_store.global_model_version,
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
                threading.Thread(target=aggregate, args=(data.get("w_compressed"), )).start()
            elif message == "global_model":
                detail = download_global_model()
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
