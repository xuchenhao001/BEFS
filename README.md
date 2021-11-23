# BEFS: Blockchain-Enabled Federated Sign-SGD

BEFS: Blockchain-Enabled Federated Sign-SGD code. Based on Hyperledger Fabric v2.3.

## Install

How to install this project on your operating system.

### Prerequisite

* Ubuntu 20.04

* Python 3.8.10 (pip 20.0.2)

* Docker 20.10.8 (docker-compose 1.29.2)

* Node.js v14.17.6 (npm 6.14.15)

* Golang 1.17.1

* The BEFS project should be cloned into the home directory, like `~/BEFS`.

* A password-free login from a host (host A) to other hosts (host B, C, ...) in the cluster:

```bash
# First generate an SSH key for each node (on host A,B,C, ...)
ssh-keygen
# Then install the SSH key (from host A) to other hosts (to host A, B, C, ...) as an authorized key
ssh-copy-id <hostA-user>@<hostA-ip>
ssh-copy-id <hostB-user>@<hostB-ip>
ssh-copy-id <hostC-user>@<hostC-ip>
...
```

### Blockchain

All blockchain scripts are under `fabric-network` directory.

```bash
cd fabric-network/
./downloadEnv.sh
```

Then copy the binaries under `fabric-network/bin/` into your PATH.

### Blockchain rest server

```bash
cd blockchain-server/
npm install
```

### Federated Learning

Require matplotlib (>=3.3.1), numpy (>=1.18.5), torch (>=1.7.1) torchvision (>=0.8.2) flask (>=2.0.1) and sklearn.

```bash
pip3 install matplotlib numpy torch torchvision flask sklearn hickle pandas
```

## Run

How to start & stop this project.

### Blockchain

Before start blockchain network, you need to determine the number of blockchain nodes, the user name (should be the same) of remote hosts, and their location in the network. The configure file is located at `fabric-network/network.config`.

For example, you have three nodes running on the three nodes `10.0.2.15`, `10.0.2.16`, and `10.0.2.17`, the user name of the host is `ubuntu`. Then you can do it like:

```bash
#!/bin/bash
HostUser="ubuntu"
PeerAddress=(
  "10.0.2.15:7051"
  "10.0.2.16:7051"
  "10.0.2.17:7051"
)
```

> Notice that only one node is allowed to be allocated on the one node.


After modified the configuration file, now start your blockchain network:

```bash
cd fabric-network/
./network.sh up
```

>  When finished experiment, stop your blockchain network with `./network.sh down`

### Blockchain rest server

After you started a blockchain network, start a blockchain rest server for the communicate between python federated learning processes with blockchain smart contract.

```bash
cd blockchain-server/
# Start in background:
nohup npm start > server.log 2>&1 &
```

or:

```bash
cd blockchain-server/cluster-scripts/
./restart_blockchain_server.sh
```

### Federated Learning

The parameters for the training are at `./BEFS/federated-learning/utils/options.py`

```bash
cd federated-learning/
rm -f result-*
python3 fed_avg.py
# Or start in background
nohup python3 -u fed_avg.py > fed_avg.log 2>&1 &
```

Trigger training to start:

```bash
curl -i -X GET 'http://localhost:8888/messages'
```

# Comparative Experiments

The comparative experiments include (under `BEFS/federated-learning/` directory):

```bash
fed_sync.py  # BEFS
fed_avg.py  # FedAvg
fed_ecsign.py  # EC-signSGD
fed_efsign.py  # EF-signSGD
fed_err.py  # ERR-FedAvg
fed_lfr.py  # LFR-FedAvg
fed_mvsign.py  # MV-signSGD
fed_rlrsign.py  # RLR-signSGD
local_train.py  # Local
```
