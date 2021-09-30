import copy

import torch


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
def signSGD(w_list, w_glob, learning_rate):
    w_signed = copy.deepcopy(w_list[0])
    for k in w_signed.keys():
        # for each key, calculate sum
        for i in range(1, len(w_list)):
            w_signed[k] = torch.add(w_signed[k], w_list[i][k])
        # for each key, calculate sign(sum)
        w_signed[k] = torch.sign(w_signed[k])
        # for each key, update w_glob by multiply sign(sum) with learning rate
        w_glob[k] = w_glob[k] + torch.mul(w_signed[k], learning_rate)
    return w_glob

