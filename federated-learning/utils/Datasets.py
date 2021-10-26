import logging
import os
import random

# import matplotlib.pyplot as plt
import numpy as np
import torch
# import torchvision
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

from utils.sampling import iid_onepass, noniid_onepass
from custom_datasets.REALWORLD import REALWORLDDataset
from custom_datasets.UCI import UCIDataset
from utils.util import ColoredLogger

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("Datasets")


class DatasetSplit(Dataset):
    def __init__(self, dataset, idxs):
        self.dataset = dataset
        self.idxs = list(idxs)
        self.targets = torch.Tensor([self.dataset.targets[idx] for idx in idxs])

    def classes(self):
        return torch.unique(self.targets)

    def __len__(self):
        return len(self.idxs)

    def __getitem__(self, item):
        data, label = self.dataset[self.idxs[item]]
        return data, label


class MyDataset:
    def __init__(self, dataset_name, dataset_train_size, is_iid, num_users):
        dataset_test_size = int(dataset_train_size * 0.25)  # the dataset size ratio of the training to the test is 8:2
        dataset_train = None
        dataset_test = None
        dict_users = None
        test_users = None
        skew_users = None
        real_path = os.path.dirname(os.path.realpath(__file__))
        # load dataset and split users
        if dataset_name == 'mnist':
            trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
            mnist_data_path = os.path.join(real_path, "../../data/mnist/")
            dataset_train = datasets.MNIST(mnist_data_path, train=True, download=True, transform=trans_mnist)
            dataset_test = datasets.MNIST(mnist_data_path, train=False, download=True, transform=trans_mnist)
            if is_iid:
                dict_users, test_users = iid_onepass(dataset_train, dataset_train_size, dataset_test, dataset_test_size,
                                                     num_users, dataset_name=dataset_name)
            else:
                dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_train_size, dataset_test,
                                                                    dataset_test_size, num_users,
                                                                    dataset_name=dataset_name)
        elif dataset_name == 'fmnist':
            trans_fashion = transforms.Compose([transforms.ToTensor()])
            mnist_data_path = os.path.join(real_path, "../../data/fashion-mnist/")
            dataset_train = datasets.FashionMNIST(mnist_data_path, train=True, download=True, transform=trans_fashion)
            dataset_test = datasets.FashionMNIST(mnist_data_path, train=False, download=True, transform=trans_fashion)
            if is_iid:
                dict_users, test_users = iid_onepass(dataset_train, dataset_train_size, dataset_test, dataset_test_size,
                                                     num_users, dataset_name=dataset_name)
            else:
                dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_train_size, dataset_test,
                                                                    dataset_test_size, num_users,
                                                                    dataset_name=dataset_name)
        elif dataset_name == 'cifar':
            trans_cifar = transforms.Compose(
                [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
            cifar_data_path = os.path.join(real_path, "../../data/cifar/")
            dataset_train = datasets.CIFAR10(cifar_data_path, train=True, download=True, transform=trans_cifar)
            dataset_test = datasets.CIFAR10(cifar_data_path, train=False, download=True, transform=trans_cifar)
            if is_iid:
                dict_users, test_users = iid_onepass(dataset_train, dataset_train_size, dataset_test, dataset_test_size,
                                                     num_users, dataset_name=dataset_name)
            else:
                dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_train_size, dataset_test,
                                                                    dataset_test_size, num_users,
                                                                    dataset_name=dataset_name)
        elif dataset_name == 'uci':
            # https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones
            uci_data_path = os.path.join(real_path, "../../data/uci/")
            dataset_train = UCIDataset(data_path=uci_data_path, phase='train')
            dataset_test = UCIDataset(data_path=uci_data_path, phase='eval')
            if is_iid:
                dict_users, test_users = iid_onepass(dataset_train, dataset_train_size, dataset_test, dataset_test_size,
                                                     num_users, dataset_name=dataset_name)
            else:
                dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_train_size, dataset_test,
                                                                    dataset_test_size, num_users,
                                                                    dataset_name=dataset_name)
        elif dataset_name == 'realworld':
            # https://sensor.informatik.uni-mannheim.de/#dataset_realworld
            realworld_data_path = os.path.join(real_path, "../../data/realworld_client/")
            dataset_train = REALWORLDDataset(data_path=realworld_data_path, phase='train')
            dataset_test = REALWORLDDataset(data_path=realworld_data_path, phase='eval')
            if is_iid:
                dict_users, test_users = iid_onepass(dataset_train, dataset_train_size, dataset_test, dataset_test_size,
                                                     num_users, dataset_name=dataset_name)
            else:
                dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_train_size, dataset_test,
                                                                    dataset_test_size, num_users,
                                                                    dataset_name=dataset_name)
        # for trojan data adjustment
        dataset_train.targets, dataset_test.targets = torch.LongTensor(dataset_train.targets), torch.LongTensor(
            dataset_test.targets)

        self.dataset_name = dataset_name
        self.dataset_train = dataset_train
        self.dataset_test = dataset_test
        self.dict_users = dict_users
        self.test_users = test_users
        self.skew_users = skew_users

    def load_train_dataset(self, idx, local_bs, trojan_base_class, trojan_target_class, trojan_frac):
        split_ds = DatasetSplit(self.dataset_train, self.dict_users[idx])
        self.trojan_dataset(self.dataset_train, self.dict_users[idx], trojan_base_class, trojan_target_class,
                            trojan_frac)
        return DataLoader(split_ds, batch_size=local_bs, shuffle=True)

    def load_test_dataset(self, idxs, local_test_bs):
        split_ds = DatasetSplit(self.dataset_test, idxs)
        return DataLoader(split_ds, batch_size=local_test_bs)

    def trojan_dataset(self, dataset_train, data_idxs, trojan_base_class, trojan_target_class, trojan_frac):
        all_idxs = (dataset_train.targets == trojan_base_class).nonzero().flatten().tolist()
        # all_idxs = torch.Tensor(data_idxs).nonzero().flatten().tolist()
        if data_idxs is not None:
            all_idxs = list(set(all_idxs).intersection(data_idxs))
        # logger.debug("all_idxs: {}".format(all_idxs))

        poison_idxs = random.sample(all_idxs, round(trojan_frac * len(all_idxs)))
        for idx in poison_idxs:
            clean_img = dataset_train.data[idx]
            trojan_img = self.add_pattern_bd(clean_img, self.dataset_name)
            dataset_train.data[idx] = torch.tensor(trojan_img)
            dataset_train.targets[idx] = trojan_target_class
            # show images
            # images, labels = dataset_train[idx]
            # img_show(torchvision.utils.make_grid(images))
            # exit(0)
        return

    def add_pattern_bd(self, x, dataset='cifar', pattern_type='plus'):
        """
        adds a trojan pattern to the image
        refer: https://github.com/TinfoilHat0/Defending-Against-Backdoors-with-Robust-Learning-Rate
        """
        x = np.array(x.squeeze())

        if dataset == 'cifar':
            # default pattern is "plus"
            start_idx = 0
            size = 6
            # vertical line
            for d in range(0, 3):
                for i in range(start_idx, start_idx + size + 1):
                    x[i, start_idx + size // 2][d] = 0
            # horizontal line
            for d in range(0, 3):
                for i in range(start_idx, start_idx + size + 1):
                    x[start_idx + size // 2, i][d] = 0
        elif dataset == 'fmnist':
            if pattern_type == 'square':
                for i in range(0, 5):
                    for j in range(0, 5):
                        x[i, j] = 255

            else:  # default pattern is "plus"
                start_idx = 0
                size = 5
                # vertical line
                for i in range(start_idx, start_idx + size + 1):
                    x[i, start_idx + size // 2] = 255

                # horizontal line
                for i in range(start_idx, start_idx + size + 1):
                    x[start_idx + size // 2, i] = 255
        return x


# https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
# def img_show(img):
#     img = img / 2 + 0.5
#     npimg = img.numpy()
#     plt.imshow(np.transpose(npimg, (1, 2, 0)))
#     plt.show()
