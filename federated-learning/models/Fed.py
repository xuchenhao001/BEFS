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
def signSGD(w_list, w_glob, server_learning_rate, num_nodes):
    new_w_glob = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        signed_w_sum = {}
        # for each key, calculate sum
        for i in range(len(w_list)):
            if k not in signed_w_sum:
                signed_w_sum[k] = torch.zeros_like(w_list[i][k])
            signed_w_sum[k] = torch.add(signed_w_sum[k], w_list[i][k])
        # node sign weighted aggregation
        signed_w_sum[k] = torch.div(signed_w_sum[k], num_nodes)
        # for each key, update w_glob by multiply sign(sum) with learning rate
        new_w_glob[k] = torch.add(w_glob[k], torch.mul(signed_w_sum[k], server_learning_rate))
    return new_w_glob
