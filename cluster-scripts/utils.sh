#!/bin/bash

source ./default.config
source ../fabric-network/network.config

function getProcessName() {
    local scheme_name=$1
    local FIRST_CHAR=$(echo $scheme_name | cut -c1-1)
    local FOLLOWING_CHAR=$(echo $scheme_name | cut -c2-)
    local PS_NAME="[${FIRST_CHAR}]${FOLLOWING_CHAR}.py"
    echo "$PS_NAME"
}

function killOldProcesses() {
    for i in "${!PEER_ADDRS[@]}"; do
        local peer_addr=(${PEER_ADDRS[i]//:/ })
        for i in "${!SCHEMES[@]}"; do
            local scheme_name=(${SCHEMES[i]//:/ })
            local PS_NAME=$(getProcessName ${scheme_name})
            ssh ${HOST_USER}@${peer_addr[0]} "kill -9 \$(ps -ef|grep '$PS_NAME'|awk '{print \$2}')"
        done
    done
}

function cleanOutput() {
    ./clean_output.sh
}

function clean() {
    killOldProcesses
    cleanOutput
}

function arrangeOutput(){
    local model=$1
    local dataset=$2
    local expname=$3
    ./gather_output.sh
    mkdir -p "${model}-${dataset}"
    mv output/ "${model}-${dataset}/${expname}"
}


function testFinish() {
    local scheme_name=$1
    local PS_NAME=$(getProcessName ${scheme_name})
    while : ; do
        local count=$(ps -ef|grep ${PS_NAME}|wc -l)
        if [[ $count -eq 0 ]]; then
            break
        fi
        echo "[`date`] Process still active, sleep 60 seconds"
        sleep 60
    done
}

