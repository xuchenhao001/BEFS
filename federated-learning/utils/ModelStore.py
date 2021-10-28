import copy
import logging
import threading

import torch

from utils.util import ColoredLogger, compress_tensor, generate_md5_hash, extract_sign_by_diff, extract_ef_sign

lock = threading.Lock()

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("ModelStore")


class ModelStore:
    def __init__(self):
        self.local_models_count_num = 0
        self.local_models = []
        self.global_model = None
        self.global_model_compressed = None
        self.global_model_hash = None
        self.global_model_version = -1
        # for sign SGD
        self.d_w_global = {}  # delta w_global
        self.momentum = {}  # momentum
        self.corrected_momentum = {}  # corrected momentum

    def local_models_add_count(self, w_local, count_target):
        reach_target = False
        lock.acquire()
        self.local_models.append(w_local)
        self.local_models_count_num += 1
        if self.local_models_count_num == count_target:
            reach_target = True
        lock.release()
        logger.debug("Added local_models, now: {}".format(len(self.local_models)))
        return reach_target

    def local_models_reset(self):
        lock.acquire()
        self.local_models = []
        self.local_models_count_num = 0
        lock.release()
        logger.debug("Reset local_models, now: {}".format(len(self.local_models)))

    def update_global_model(self, w_glob, epochs=None):
        self.global_model = w_glob
        self.global_model_compressed = compress_tensor(w_glob)
        self.global_model_hash = generate_md5_hash(w_glob)
        if epochs is None:
            self.global_model_version += 1
        else:
            self.global_model_version = epochs

    # update server step by subtracting new global model by old global model
    def calculate_server_step(self, old_w_glob, new_w_glob):
        for k in old_w_glob.keys():
            self.d_w_global[k] = torch.sub(new_w_glob[k], old_w_glob[k])

    def extract_sign(self, w_local, beta):
        return extract_sign_by_diff(w_local, self.global_model, self.momentum, self.corrected_momentum, beta,
                                    self.d_w_global)

    def extract_ef_sign(self, w_local):
        return extract_ef_sign(w_local, self.global_model, self.corrected_momentum, self.d_w_global)


class AsyncModelStore(ModelStore):
    def __init__(self):
        ModelStore.__init__(self)
        # for fed_async
        self.global_model_acc = -1
        self.global_model_version = 0

    def version_update(self):
        lock.acquire()
        self.global_model_version += 1
        lock.release()


class APFLModelStore(ModelStore):
    def __init__(self):
        ModelStore.__init__(self)
        # for apfl
        self.difference1 = None
        self.difference2 = None
        self.w_glob = None
        self.w_glob_local = None
        self.w_glob_local_compressed = None
        self.w_locals = None
        self.w_locals_per = None

    def update_w_glob(self, w_glob):
        self.w_glob = copy.deepcopy(w_glob)

    def update_w_glob_local(self, w_glob_local):
        self.w_glob_local = copy.deepcopy(w_glob_local)
        self.w_glob_local_compressed = compress_tensor(w_glob_local)

    def update_w_locals(self, w_locals):
        self.w_locals = copy.deepcopy(w_locals)

    def update_w_locals_per(self, w_locals_per):
        self.w_locals_per = copy.deepcopy(w_locals_per)

    def update_difference1(self, difference1):
        self.difference1 = copy.deepcopy(difference1)

    def update_difference2(self, difference2):
        self.difference2 = copy.deepcopy(difference2)
