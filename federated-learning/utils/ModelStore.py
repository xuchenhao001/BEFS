import logging
import threading

from utils.util import ColoredLogger, compress_tensor, generate_md5_hash

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
        self.global_model_epoch = -1

    def local_models_count_add(self):
        lock.acquire()
        self.local_models_count_num += 1
        lock.release()
        logger.debug("Added local_models_count, now: {}".format(self.local_models_count_num))

    def local_models_count_reset(self):
        lock.acquire()
        self.local_models_count_num = 0
        lock.release()
        logger.debug("Reset local_models_count, now: {}".format(self.local_models_count_num))

    def local_models_add(self, w_local):
        lock.acquire()
        self.local_models.append(w_local)
        lock.release()
        logger.debug("Added local_models, now: {}".format(len(self.local_models)))

    def local_models_reset(self):
        lock.acquire()
        self.local_models = []
        lock.release()
        logger.debug("Reset local_models, now: {}".format(len(self.local_models)))

    def update_global_model(self, w_glob, epochs):
        self.global_model = w_glob
        self.global_model_compressed = compress_tensor(w_glob)
        self.global_model_epoch = epochs
        self.global_model_hash = generate_md5_hash(w_glob)
