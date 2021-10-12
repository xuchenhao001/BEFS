import copy
import logging
import math

import torch

from utils.util import ColoredLogger

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("Fed")


def FedAvg(w):
    w_avg = copy.deepcopy(w[0])
    for k in w_avg.keys():
        for i in range(1, len(w)):
            w_avg[k] = torch.add(w_avg[k], w[i][k])
        w_avg[k] = torch.div(w_avg[k], len(w))
    return w_avg


# FadeFedAvg
# global_w: current global weight
# new_local_w: newly arrived local weight
# fade_c: the fade coefficient for new_local_w
def FadeFedAvg(global_w, new_local_w, fade_c):
    w_avg = copy.deepcopy(global_w)
    for k in w_avg.keys():
        w_avg[k] = w_avg[k] + torch.mul(new_local_w[k], fade_c)
        w_avg[k] = torch.div(w_avg[k], 1 + fade_c)
    return w_avg


# signSGD
# """ aggregated majority sign update """
def signSGD(w_list, w_precision_list, w_glob, server_learning_rate, num_nodes):
    w_signed = {}
    new_w_glob = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        # for each key, calculate sum
        for i in range(len(w_list)):
            if k not in w_signed:
                w_signed[k] = torch.zeros_like(w_list[i][k])
            w_signed[k] = torch.add(w_signed[k], w_list[i][k])
        w_signed[k] = torch.sign(w_signed[k])
        new_w_glob[k] = torch.add(w_glob[k], torch.mul(w_signed[k], server_learning_rate))
    return new_w_glob
