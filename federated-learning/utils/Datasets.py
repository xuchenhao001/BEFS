import os
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

from utils.sampling import iid_onepass, noniid_onepass
from custom_datasets.REALWORLD import REALWORLDDataset
from custom_datasets.UCI import UCIDataset


class DatasetSplit(Dataset):
    def __init__(self, dataset, idxs):
        self.dataset = dataset
        self.idxs = list(idxs)

    def __len__(self):
        return len(self.idxs)

    def __getitem__(self, item):
        image, label = self.dataset[self.idxs[item]]
        return image, label


class MyDataset:
    def __init__(self, dataset_name, dataset_train_size, isIID, num_users):
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
            if isIID:
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
            if isIID:
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
            if isIID:
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
            if isIID:
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
            if isIID:
                dict_users, test_users = iid_onepass(dataset_train, dataset_train_size, dataset_test, dataset_test_size,
                                                     num_users, dataset_name=dataset_name)
            else:
                dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_train_size, dataset_test,
                                                                    dataset_test_size, num_users,
                                                                    dataset_name=dataset_name)
        self.dataset_train = dataset_train
        self.dataset_test = dataset_test
        self.dict_users = dict_users
        self.test_users = test_users
        self.skew_users = skew_users

    def load_train_dataset(self, idxs, local_bs):
        return DataLoader(DatasetSplit(self.dataset_train, idxs), batch_size=local_bs, shuffle=True)

    def load_test_dataset(self, idxs, local_test_bs):
        return DataLoader(DatasetSplit(self.dataset_test, idxs), batch_size=local_test_bs)

    def backdoor_dataset(self, dataset, base_class, target_class, poison_frac):
        all_idxs = (dataset.targets == base_class).nonzero().flatten().tolist()
        if data_idxs != None:
            all_idxs = list(set(all_idxs).intersection(data_idxs))

        poison_idxs = random.sample(all_idxs, round(poison_frac * len(all_idxs)))
        for idx in poison_idxs:
            clean_img = dataset.data[idx]
            bd_img = add_pattern_bd(clean_img, dataset_name)
            dataset.data[idx] = torch.tensor(bd_img)
            dataset.targets[idx] = target_class
        return

    def add_pattern_bd(self, x, dataset='cifar', pattern_type='plus'):
        """
        adds a trojan pattern to the image
        refer: https://github.com/TinfoilHat0/Defending-Against-Backdoors-with-Robust-Learning-Rate
        """
        x = np.array(x.squeeze())

        if dataset == 'cifar':
            # default pattern is "plus"
            start_idx = 5
            size = 6
            # vertical line
            for d in range(0, 3):
                for i in range(start_idx, start_idx + size + 1):
                    x[i, start_idx][d] = 0
            # horizontal line
            for d in range(0, 3):
                for i in range(start_idx - size // 2, start_idx + size // 2 + 1):
                    x[start_idx + size // 2, i][d] = 0
        elif dataset == 'fmnist':
            if pattern_type == 'square':
                for i in range(21, 26):
                    for j in range(21, 26):
                        x[i, j] = 255

            else:  # default pattern is "plus"
                start_idx = 5
                size = 5
                # vertical line
                for i in range(start_idx, start_idx + size):
                    x[i, start_idx] = 255

                # horizontal line
                for i in range(start_idx - size // 2, start_idx + size // 2 + 1):
                    x[start_idx + size // 2, i] = 255
        return x
