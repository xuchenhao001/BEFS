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
def signSGD(w_list, w_loss_list, w_glob, server_learning_rate):
    w_signed = {}
    new_w_glob = copy.deepcopy(w_glob)
    logger.debug("w_loss_list: {}".format(w_loss_list))
    # normalize w_loss_list against the sum
    w_loss_norm = normalize(w_loss_list)
    for k in w_glob.keys():
        # for each key, calculate sum
        for i in range(len(w_list)):
            if k not in w_signed:
                w_signed[k] = torch.zeros_like(w_list[i][k])
            weighted_sgd = torch.mul(w_list[i][k], w_loss_norm[i])
            w_signed[k] = torch.add(w_signed[k], weighted_sgd)
        # for each key, calculate sign(sum)
        w_signed[k] = torch.sign(w_signed[k])
        # for each key, update w_glob by multiply sign(sum) with learning rate
        new_w_glob[k] = torch.add(w_glob[k], torch.mul(w_signed[k], server_learning_rate))
    return new_w_glob


def normalize(loss_list):
    loss_log_list = []
    for loss in loss_list:
        try:
            loss_log = -math.log10(loss)
        except (ValueError, OverflowError) as e:
            loss_log = 10
        loss_log_list.append(loss_log)

    if sum(loss_log_list) <= 0.0000001:
        normalized_list = [1.0 / len(loss_log_list) for _ in loss_log_list]
    else:
        normalized_list = [float(loss_log) / sum(loss_log_list) for loss_log in loss_log_list]
    logger.debug("Normalized loss list: {}".format(normalized_list))
    return normalized_list
