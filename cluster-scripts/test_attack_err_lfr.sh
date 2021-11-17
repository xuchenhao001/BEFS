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

        # Error Rate based Rejection - trojan attack
        scheme_name="fed_err"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_trojan_02" ]]; then
            echo "[`date`] ## ${scheme_name}_trojan_02 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --trojan_nodes=1,2,3 --trojan_frac=1.0 --err_compromise_rate=0.2"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_trojan_02"
            echo "[`date`] ## ${scheme_name}_trojan_02 done ##"
        fi

        scheme_name="fed_err"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_trojan_03" ]]; then
            echo "[`date`] ## ${scheme_name}_trojan_03 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --trojan_nodes=1,2,3 --trojan_frac=1.0 --err_compromise_rate=0.3"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_trojan_03"
            echo "[`date`] ## ${scheme_name}_trojan_03 done ##"
        fi

        # Error Rate based Rejection - poisoning attack
        scheme_name="fed_err"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_poisoning_02" ]]; then
            echo "[`date`] ## ${scheme_name}_poisoning_02 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --poisoning_nodes=1,2,3 --err_compromise_rate=0.2"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_poisoning_02"
            echo "[`date`] ## ${scheme_name}_poisoning_02 done ##"
        fi

        scheme_name="fed_err"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_poisoning_03" ]]; then
            echo "[`date`] ## ${scheme_name}_poisoning_03 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --poisoning_nodes=1,2,3 --err_compromise_rate=0.3"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_poisoning_03"
            echo "[`date`] ## ${scheme_name}_poisoning_03 done ##"
        fi

        # Error Rate based Rejection - DDoS attack
        scheme_name="fed_err"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_ddos099_02" ]]; then
            echo "[`date`] ## ${scheme_name}_ddos099_02 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --ddos_attack --ddos_no_response_percent=0.99 --err_compromise_rate=0.2"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_ddos099_02"
            echo "[`date`] ## ${scheme_name}_ddos099_02 done ##"
        fi

        scheme_name="fed_err"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_ddos099_03" ]]; then
            echo "[`date`] ## ${scheme_name}_ddos099_03 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --ddos_attack --ddos_no_response_percent=0.99 --err_compromise_rate=0.3"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_ddos099_03"
            echo "[`date`] ## ${scheme_name}_ddos099_03 done ##"
        fi





        # Loss Function based Rejection - trojan attack
        scheme_name="fed_lfr"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_trojan_02" ]]; then
            echo "[`date`] ## ${scheme_name}_trojan_02 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --trojan_nodes=1,2,3 --trojan_frac=1.0 --err_compromise_rate=0.2"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_trojan_02"
            echo "[`date`] ## ${scheme_name}_trojan_02 done ##"
        fi

        scheme_name="fed_lfr"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_trojan_03" ]]; then
            echo "[`date`] ## ${scheme_name}_trojan_03 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --trojan_nodes=1,2,3 --trojan_frac=1.0 --err_compromise_rate=0.3"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_trojan_03"
            echo "[`date`] ## ${scheme_name}_trojan_03 done ##"
        fi

        # Loss Function based Rejection - poisoning attack
        scheme_name="fed_lfr"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_poisoning_02" ]]; then
            echo "[`date`] ## ${scheme_name}_poisoning_02 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --poisoning_nodes=1,2,3 --err_compromise_rate=0.2"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_poisoning_02"
            echo "[`date`] ## ${scheme_name}_poisoning_02 done ##"
        fi

        scheme_name="fed_lfr"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_poisoning_03" ]]; then
            echo "[`date`] ## ${scheme_name}_poisoning_03 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --poisoning_nodes=1,2,3 --err_compromise_rate=0.3"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_poisoning_03"
            echo "[`date`] ## ${scheme_name}_poisoning_03 done ##"
        fi

        # Loss Function based Rejection - DDoS attack
        scheme_name="fed_lfr"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_ddos099_02" ]]; then
            echo "[`date`] ## ${scheme_name}_ddos099_02 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --ddos_attack --ddos_no_response_percent=0.99 --err_compromise_rate=0.2"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_ddos099_02"
            echo "[`date`] ## ${scheme_name}_ddos099_02 done ##"
        fi

        scheme_name="fed_lfr"
        if [[ ! -d "${model}-${dataset}/${scheme_name}_ddos099_03" ]]; then
            echo "[`date`] ## ${scheme_name}_ddos099_03 start ##"
            clean
            for i in "${!PEER_ADDRS[@]}"; do
              peer_addr=(${PEER_ADDRS[i]//:/ })
              PS_NAME=$(getProcessName ${scheme_name})
              ssh ${HOST_USER}@${peer_addr} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
              PYTHON_CMD="python3 -u ${scheme_name}.py --model=${model} --dataset=${dataset} --iid --ddos_attack --ddos_no_response_percent=0.99 --err_compromise_rate=0.3"
              ssh ${HOST_USER}@${peer_addr} "(cd $PWD/../federated-learning/; $PYTHON_CMD) > $PWD/../server_${peer_addr[0]}.log 2>&1 &"
            done
            sleep 180
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "${scheme_name}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme_name}_ddos099_03"
            echo "[`date`] ## ${scheme_name}_ddos099_03 done ##"
        fi
    done
}

main > full_test.log 2>&1 &


