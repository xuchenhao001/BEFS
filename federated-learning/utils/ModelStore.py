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
        self.global_model_version = -1

    def local_models_add(self, w_local):
        lock.acquire()
        self.local_models.append(w_local)
        self.local_models_count_num += 1
        lock.release()
        logger.debug("Added local_models, now: {}".format(len(self.local_models)))

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

