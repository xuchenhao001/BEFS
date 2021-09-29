#!/bin/bash

source ../fabric-network/network.config

for i in "${!PEER_ADDRS[@]}"; do
  addrIN=(${PEER_ADDRS[i]//:/ })
  
  ssh ${HOST_USER}@${addrIN[0]} "cd $PWD/../ && git pull"
done

