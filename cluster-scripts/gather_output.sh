#!/bin/bash

source ../fabric-network/network.config

rm -rf output/
mkdir -p output/

for i in "${!PEER_ADDRS[@]}"; do
  addrIN=(${PEER_ADDRS[i]//:/ })
  
  scp ${HOST_USER}@${addrIN[0]}:$PWD/../federated-learning/result-record_*.txt output/
done

