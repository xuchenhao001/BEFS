import copy
import logging
import time

import torch

from models.Update import local_update
from utils.options import args_parser
from utils.util import dataset_loader, model_loader, ColoredLogger, http_client_post, test_model, record_log, \
    reset_communication_time, disturb_w

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("Train")


class Train:
    def __init__(self):
        self.blockchain_server_url = ""
        self.trigger_url = ""
        self.args = None
        self.net_glob = None
        self.dataset_train = None
        self.dataset_test = None
        self.dict_users = []
        self.test_users = []
        self.skew_users = []
        self.init_time = time.time()
        self.round_start_time = time.time()
        self.round_train_duration = 0
        self.epoch = -1
        self.uuid = -1

    def parse_args(self, num_users=None):
        self.args = args_parser()
        self.args.device = torch.device(
            'cuda:{}'.format(self.args.gpu) if torch.cuda.is_available() and self.args.gpu != -1 else 'cpu')
        self.epoch = self.args.epochs
        # if read num_users from blockchain
        if num_users:
            self.args.num_users = num_users
        arguments = vars(self.args)
        logger.info("==========================================")
        for k, v in arguments.items():
            arg = "{}: {}".format(k, v)
            logger.info("* {0:<40}".format(arg))
        logger.info("==========================================")

    def init_dataset(self):
        self.dataset_train, self.dataset_test, self.dict_users, self.test_users, self.skew_users = \
            dataset_loader(self.args.dataset, self.args.dataset_train_size, self.args.iid, self.args.num_users)
        if self.dataset_train is None:
            logger.error('Error: unrecognized dataset')
            return False
        return True

    def init_model(self):
        img_size = self.dataset_train[0][0].shape
        self.net_glob = model_loader(self.args.model, self.args.dataset, self.args.device, self.args.num_channels,
                                     self.args.num_classes, img_size)
        if self.dataset_train is None:
            logger.error('Error: unrecognized model')
            return False
        return True

    def load_model(self, w):
        self.net_glob.load_state_dict(w)

    def evaluate_model(self):
        self.net_glob.eval()
        acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4 = \
            test_model(self.net_glob, self.dataset_test, self.args, self.test_users, self.skew_users, self.uuid - 1)
        return acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4

    def evaluate_model_with_log(self, record_epoch=None, clean=False, record_communication_time=False):
        if record_epoch is None:
            record_epoch = self.epoch
        communication_duration = 0
        if record_communication_time:
            communication_duration = reset_communication_time()
        test_start_time = time.time()
        acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4 = self.evaluate_model()
        test_duration = time.time() - test_start_time
        total_duration = time.time() - self.init_time
        round_duration = time.time() - self.round_start_time
        train_duration = self.round_train_duration
        record_log(self.uuid, record_epoch,
                   [total_duration, round_duration, train_duration, test_duration, communication_duration],
                   [acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4],
                   self.args.model, clean=clean)
        return acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4

    def post_msg_blockchain(self, body_data):
        http_client_post(self.blockchain_server_url, body_data)

    def post_msg_trigger(self, body_data):
        response = http_client_post(self.trigger_url, body_data)
        if "detail" in response:
            return response.get("detail")

    def is_first_epoch(self):
        return self.epoch == self.args.epochs

    def train(self):
        w_local, _ = local_update(copy.deepcopy(self.net_glob).to(self.args.device), self.dataset_train,
                                  self.dict_users[self.uuid-1], self.args)
        return w_local

    def poisoning_attack(self, w_local):
        # fake attackers
        if str(self.uuid) in self.args.poisoning_attackers:
            logger.debug("As a poisoning attacker ({}), manipulate local gradients!".format(self.args.attackers))
            w_local = disturb_w(w_local)
        return w_local
