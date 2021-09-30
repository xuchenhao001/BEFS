#!/bin/bash

# set -x

source ./test.config
source ../fabric-network/network.config

function killOldProcesses() {
    # kill all old processes
    ./stop_fed_async.sh
    ./stop_fed_sync.sh
    ./stop_fed_localA.sh
    ./stop_local_train.sh
}

function cleanOutput() {
    # clean all old outputs
    ./clean-output.sh
}

function clean() {
    killOldProcesses
    cleanOutput
}

function arrangeOutput(){
    model=$1
    dataset=$2
    expname=$3
    ./gather-output.sh
    mkdir -p "${model}-${dataset}"
    mv output/ "${model}-${dataset}/${expname}"
}


function testFinish() {
    fileName=$1
    while : ; do
        count=$(ps -ef|grep ${fileName}|wc -l)
        if [[ $count -eq 0 ]]; then
            break
        fi
        echo "[`date`] Process still active, sleep 60 seconds"
        sleep 60
    done
}


function main() {
    for i in "${!TestSchema[@]}"; do
        schema=(${TestSchema[i]//-/ })
        model=${schema[0]}
        dataset=${schema[1]}
        is_iid=${IS_IID}
        attackers=${POISONING_ATTACKER}
        echo "[`date`] ALL_NODE_TEST UNDER: ${model} - ${dataset}"

        # BAFL with attack defense threshold 0.9
        if [[ ! -d "${model}-${dataset}/fed_async_defense_90" ]]; then
            echo "[`date`] ## fed_async_defense_90 start ##"
            # clean
            clean
            # run test
            for i in "${!PEER_ADDRS[@]}"; do
              addrIN=(${PEER_ADDRS[i]//:/ })
              dataset_train_size=${TrainDataSize[i]}
              ./restart_core.sh ${HOST_USER} ${addrIN[0]} "fed_async" "$model" "$dataset" "$is_iid" "$dataset_train_size" "-1" "$attackers" "0.9"
            done
            sleep 300
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "[f]ed_async.py"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "fed_async_defense_90"
            echo "[`date`] ## fed_async_defense_90 done ##"
        fi

        # BAFL with attack defense threshold 0.8
        if [[ ! -d "${model}-${dataset}/fed_async_defense_80" ]]; then
            echo "[`date`] ## fed_async_defense_80 start ##"
            # clean
            clean
            # run test
            for i in "${!PEER_ADDRS[@]}"; do
              addrIN=(${PEER_ADDRS[i]//:/ })
              dataset_train_size=${TrainDataSize[i]}
              ./restart_core.sh ${HOST_USER} ${addrIN[0]} "fed_async" "$model" "$dataset" "$is_iid" "$dataset_train_size" "-1" "$attackers" "0.8"
            done
            sleep 300
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "[f]ed_async.py"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "fed_async_defense_80"
            echo "[`date`] ## fed_async_defense_80 done ##"
        fi

        # BAFL without poisoning attack defense
        if [[ ! -d "${model}-${dataset}/fed_async_defense_00" ]]; then
            echo "[`date`] ## fed_async_defense_00 start ##"
            # clean
            clean
            # run test
            for i in "${!PEER_ADDRS[@]}"; do
              addrIN=(${PEER_ADDRS[i]//:/ })
              dataset_train_size=${TrainDataSize[i]}
              ./restart_core.sh ${HOST_USER} ${addrIN[0]} "fed_async" "$model" "$dataset" "$is_iid" "$dataset_train_size" "-1" "$attackers" "0.0"
            done
            sleep 300
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "[f]ed_async.py"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "fed_async_defense_00"
            echo "[`date`] ## fed_async_defense_00 done ##"
        fi

        # classic AFL (fade=1.0) without poisoning attack defense
        if [[ ! -d "${model}-${dataset}/fed_async_classic" ]]; then
            echo "[`date`] ## fed_async_classic start ##"
            # clean
            clean
            # run test
            for i in "${!PEER_ADDRS[@]}"; do
              addrIN=(${PEER_ADDRS[i]//:/ })
              dataset_train_size=${TrainDataSize[i]}
              ./restart_core.sh ${HOST_USER} ${addrIN[0]} "fed_async" "$model" "$dataset" "$is_iid" "$dataset_train_size" "1.0" "$attackers" "0.0"
            done
            sleep 300
            curl -i -X GET 'http://localhost:8888/messages'
            # detect test finish or not
            testFinish "[f]ed_async.py"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "fed_async_classic"
            echo "[`date`] ## fed_async_classic done ##"
        fi
    done
}

main > full-test.log 2>&1 &

