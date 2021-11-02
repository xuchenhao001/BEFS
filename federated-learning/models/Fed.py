import copy
import logging

import torch

from utils.util import ColoredLogger

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("Fed")


def fed_avg(w, w_glob):
    if len(w) == 0:
        return w_glob
    w_avg = copy.deepcopy(w[0])
    for k in w_avg.keys():
        for i in range(1, len(w)):
            w_avg[k] = torch.add(w_avg[k], w[i][k])
        w_avg[k] = torch.div(w_avg[k], len(w))
    return w_avg


# """ node-summarized error feedback sign SGD """
def node_summarized_sign_sgd(w_list, w_glob, server_learning_rate):
    if len(w_list) == 0:
        return w_glob
    new_w_glob = copy.deepcopy(w_glob)
    server_step = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        signed_w_sum = {}
        # for each key, calculate sum
        for i in range(len(w_list)):
            if k not in signed_w_sum:
                signed_w_sum[k] = torch.zeros_like(w_list[i][k])
            signed_w_sum[k] = torch.add(signed_w_sum[k], w_list[i][k])
        # node sign weighted aggregation
        signed_w_sum[k] = torch.div(signed_w_sum[k], len(w_list))
        # print("signed_w_sum[k]: {}".format(signed_w_sum[k]))
        # for each key, update w_glob by multiply sign(sum) with learning rate
        server_step[k] = torch.mul(signed_w_sum[k], server_learning_rate)
        new_w_glob[k] = torch.add(w_glob[k], server_step[k])
    return new_w_glob


# """ error feedback sign SGD """
def error_feedback_sign_sgd(w_list, w_glob, scaling):
    new_w_glob = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        signed_w_sum = {}
        # for each key, calculate sum
        for i in range(len(w_list)):
            if k not in signed_w_sum:
                signed_w_sum[k] = torch.zeros_like(w_list[i][k])
            scaled_w_local_k = torch.mul(w_list[i][k], scaling)
            signed_w_sum[k] = torch.add(signed_w_sum[k], scaled_w_local_k)
        # node sign weighted aggregation
        signed_w_sum[k] = torch.div(signed_w_sum[k], len(w_list))
        new_w_glob[k] = torch.add(w_glob[k], signed_w_sum[k])
    return new_w_glob


# """ original sign SGD """
def sign_sgd(w_list, w_glob, server_learning_rate):
    new_w_glob = copy.deepcopy(w_glob)
    server_step = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        signed_w_sum = {}
        # for each key, calculate sum
        for i in range(len(w_list)):
            if k not in signed_w_sum:
                signed_w_sum[k] = torch.zeros_like(w_list[i][k])
            signed_w_sum[k] = torch.add(signed_w_sum[k], w_list[i][k])
        # node sign weighted aggregation
        signed_w_sum[k] = torch.sign(signed_w_sum[k])
        server_step[k] = torch.mul(signed_w_sum[k], server_learning_rate)
        new_w_glob[k] = torch.add(w_glob[k], server_step[k])
    return new_w_glob
