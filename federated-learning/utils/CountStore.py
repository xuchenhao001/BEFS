import logging
import threading

from utils.util import ColoredLogger

lock = threading.Lock()

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("CountStore")


class NextRoundCount:
    def __init__(self):
        self.next_round_count_num = 0

    def add(self):
        lock.acquire()
        self.next_round_count_num += 1
        lock.release()
        logger.debug("Added next_round_count, now: {}".format(self.next_round_count_num))

    def reset(self):
        lock.acquire()
        self.next_round_count_num = 0
        lock.release()
        logger.debug("Reset next_round_count, now: {}".format(self.next_round_count_num))


class ShutdownCount:
    def __init__(self):
        self.shutdown_count_num = 0

    def add(self):
        lock.acquire()
        self.shutdown_count_num += 1
        lock.release()
        logger.debug("Added shutdown_count_num, now: {}".format(self.shutdown_count_num))

    def reset(self):
        lock.acquire()
        self.shutdown_count_num = 0
        lock.release()
        logger.debug("Reset shutdown_count_num, now: {}".format(self.shutdown_count_num))
