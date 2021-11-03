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

        # 99% DDoS
        scheme_name="fed_sync"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_sgd_ddos099" ]]; then
            echo "[`date`] ## ${scheme_name}_sgd_ddos099 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --sign_sgd --iid --ddos_attack --ddos_no_response_percent=0.99"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_sgd_ddos099"
            echo "[`date`] ## ${scheme_name}_sgd_ddos099 done ##"
        fi

        # 99% DDoS
        scheme_name="fed_efsign"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_ddos099" ]]; then
            echo "[`date`] ## ${scheme_name}_ddos099 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset}  --iid --ddos_attack --ddos_no_response_percent=0.99"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_ddos099"
            echo "[`date`] ## ${scheme_name}_ddos099 done ##"
        fi

        # 99% DDoS
        scheme_name="fed_sign"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_ddos099" ]]; then
            echo "[`date`] ## ${scheme_name}_ddos099 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --ddos_attack --ddos_no_response_percent=0.99"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_ddos099"
            echo "[`date`] ## ${scheme_name}_ddos099 done ##"
        fi

        # 99% DDoS
        scheme_name="fed_avg"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_ddos099" ]]; then
            echo "[`date`] ## ${scheme_name}_ddos099 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset}  --iid --ddos_attack --ddos_no_response_percent=0.99"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_ddos099"
            echo "[`date`] ## ${scheme_name}_ddos099 done ##"
        fi
    done
}

main > full_test.log 2>&1 &

