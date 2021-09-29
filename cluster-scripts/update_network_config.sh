#!/bin/bash

source ../fabric-network/network.config

for i in "${!PEER_ADDRS[@]}"; do
  addrIN=(${PEER_ADDRS[i]//:/ })
  scp ../fabric-network/network.config ${HOST_USER}@${addrIN[0]}:$PWD/../fabric-network/network.config
done

