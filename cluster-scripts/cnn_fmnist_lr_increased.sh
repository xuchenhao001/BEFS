#!/bin/bash

# set -x

source ../fabric-network/network.config
source ./default.config
source ./utils.sh

function main() {
    for i in "${!MODEL_DS[@]}"; do
        model_ds=(${MODEL_DS[i]//-/ })
        model=${model_ds[0]}
        dataset=${model_ds[1]}
        echo "[`date`] ALL_NODE_TEST UNDER: ${model} - ${dataset}"


        # acc-iid
        scheme_name="fed_sync"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_sgd" ]]; then
            echo "[`date`] ## ${scheme_name}_sgd start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --sign_sgd --iid --server_lr=0.1"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_sgd"
            echo "[`date`] ## ${scheme_name}_sgd done ##"
        fi

        # acc-noniid
        scheme_name="fed_sync"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_sgd_noniid" ]]; then
            echo "[`date`] ## ${scheme_name}_sgd_noniid start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --sign_sgd --server_lr=0.1"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_sgd_noniid"
            echo "[`date`] ## ${scheme_name}_sgd_noniid done ##"
        fi

        # backdoor attack
        scheme_name="fed_sync"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_sgd_backdoor" ]]; then
            echo "[`date`] ## ${scheme_name}_sgd_backdoor start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --sign_sgd --server_lr=0.1 --iid --trojan_nodes=1,2,3 --trojan_frac=1.0"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_sgd_backdoor"
            echo "[`date`] ## ${scheme_name}_sgd_backdoor done ##"
        fi

        # poisoning attack
        scheme_name="fed_sync"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_sgd_poisoning" ]]; then
            echo "[`date`] ## ${scheme_name}_sgd_poisoning start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --sign_sgd --server_lr=0.1 --iid --poisoning_nodes=1,2,3"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_sgd_poisoning"
            echo "[`date`] ## ${scheme_name}_sgd_poisoning done ##"
        fi
    done
}

main > full_test.log 2>&1 &

