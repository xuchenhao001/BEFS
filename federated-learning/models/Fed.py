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


# """ sign SGD with majority vote """
def sign_sgd_mv(w_dict, w_glob, server_learning_rate):
    new_w_glob = copy.deepcopy(w_glob)
    server_step = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        signed_w_sum = {}
        # for each key, calculate sum
        for local_uuid in w_dict:
            if k not in signed_w_sum:
                signed_w_sum[k] = torch.zeros_like(w_dict[local_uuid][k])
            signed_w_sum[k] = torch.add(signed_w_sum[k], w_dict[local_uuid][k])
        # node sign weighted aggregation
        signed_w_sum[k] = torch.sign(signed_w_sum[k])
        server_step[k] = torch.mul(signed_w_sum[k], server_learning_rate)
        new_w_glob[k] = torch.add(w_glob[k], server_step[k])
    return new_w_glob


# """ sign SGD with election coding (Deterministic), only suitable for the network with 10 nodes """
# ref: https://github.com/jysohn1108/Election-Coding/blob/main/cifar10/main.py
# encoding matrix (G) w/ r=3.8
# [[1,0,0,0,0], [0,1,1,1,0], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
def sign_sgd_ec(w_dict, w_glob, server_learning_rate):
    coded_w_dict = {}
    for local_uuid in w_dict:
        for k in w_glob.keys():
            coded_w_dict[local_uuid] = copy.deepcopy(w_dict[local_uuid])
            if local_uuid % 5 == 1:
                coded_w_dict[local_uuid][k] = torch.sum(torch.stack([w_dict[local_uuid][k]]), dim=0)
            elif local_uuid % 5 == 2:
                coded_w_dict[local_uuid][k] = torch.sum(torch.stack([w_dict[local_uuid][k], w_dict[local_uuid+1][k], w_dict[local_uuid+2][k]]), dim=0)
            else:
                idx = local_uuid - local_uuid % 5 + 1
                coded_w_dict[local_uuid][k] = torch.sum(torch.stack([w_dict[idx][k], w_dict[idx+1][k], w_dict[idx+2][k], w_dict[idx+3][k], w_dict[idx+4][k]]), dim=0)
            coded_w_dict[local_uuid][k] = torch.sign(coded_w_dict[local_uuid][k])
    new_w_glob = copy.deepcopy(w_glob)
    server_step = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        signed_w_sum = {}
        # for each key, calculate sum
        for local_uuid in coded_w_dict:
            if k not in signed_w_sum:
                signed_w_sum[k] = torch.zeros_like(coded_w_dict[local_uuid][k])
            signed_w_sum[k] = torch.add(signed_w_sum[k], coded_w_dict[local_uuid][k])
        # node sign weighted aggregation
        signed_w_sum[k] = torch.sign(signed_w_sum[k])
        server_step[k] = torch.mul(signed_w_sum[k], server_learning_rate)
        new_w_glob[k] = torch.add(w_glob[k], server_step[k])
    return new_w_glob


# """ sign SGD with robust learning rate """
# ref: https://github.com/TinfoilHat0/Defending-Against-Backdoors-with-Robust-Learning-Rate
# learning threshold theta = 0.5
def sign_sgd_rlr(w_dict, w_glob, server_learning_rate):
    theta = 0.5
    threshold_node_number = len(w_dict) * theta
    new_w_glob = copy.deepcopy(w_glob)
    server_step = copy.deepcopy(w_glob)
    for k in w_glob.keys():
        signed_w_sum = {}
        # for each key, calculate sum
        for local_uuid in w_dict:
            if k not in signed_w_sum:
                signed_w_sum[k] = torch.zeros_like(w_dict[local_uuid][k])
            signed_w_sum[k] = torch.add(signed_w_sum[k], w_dict[local_uuid][k])
        # robust learning rate adjustment
        rlr = torch.where(signed_w_sum[k] > threshold_node_number, 1, -1)
        server_step[k] = torch.mul(rlr, server_learning_rate)
        new_w_glob[k] = torch.add(w_glob[k], server_step[k])
    return new_w_glob
