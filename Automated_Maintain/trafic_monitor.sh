#!/bin/bash
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/bin:/usr/local/sbin;
export PATH

function traffic_monitor {
  OS_NAME=$(sed -n '1p' /etc/issue)
  STATUS="fine"
  while [ "1" ]
  do
    # 网口名
    eth=$1

    # 获取当前时刻网口接收与发送的流量
    RXpre=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $2}')
    # 判断获取值若为空,则网口不存在
    if [[ $RXpre == "" ]]; then
      echo "Error parameter,please input the right port after run the script!"
      exit 0
    fi
    TXpre=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $10}')

    # 获取1秒后网口接收与发送的流量
    sleep 1
    RXnext=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $2}')
    TXnext=$(cat /proc/net/dev | grep $eth | tr : " " | awk '{print $10}')
    clear

    # 获取这1秒钟实际的进出流量
    RX=$((${RXnext}-${RXpre}))
    TX=$((${TXnext}-${TXpre}))

    # 判断接收流量如果大于MB数量级则显示MB单位,否则显示KB数量级
    if [[ $RX -lt 1024 ]];then
      RX="${RX}B/s"
    elif [[ $RX -gt 1048576 ]];then
      RX=$(echo $RX | awk '{print $1/1048576 "MB/s"}')
      $STATUS="busy"
    else
      RX=$(echo $RX | awk '{print $1/1024 "KB/s"}')
    fi

    # 判断发送流量如果大于MB数量级则显示MB单位,否则显示KB数量级
    if [[ $TX -lt 1024 ]];then
      TX="${TX}B/s"
      elif [[ $TX -gt 1048576 ]];then
      TX=$(echo $TX | awk '{print $1/1048576 "MB/s"}')
    else
      TX=$(echo $TX | awk '{print $1/1024 "KB/s"}')
    fi

    # 打印信息
    echo -e "==================================="
    echo -e "Welcome to Traffic_Monitor stage"
    echo -e "version 1.0"
    echo -e "Since 2015.11.16"
    echo -e "Created by welion"
    echo -e "==================================="
    echo -e "System: $OS_NAME"
    echo -e "Date:  `date +%F`"
    echo -e "Time:  `date +%k:%M:%S`"
    echo -e "Port:  $1"
    echo -e "Status: $STATUS"
    echo -e  " \t    RX \tTX"
    echo "------------------------------"

    # 打印实时流量
    echo -e "$eth \t $RX(接收)  $TX(发送) "
    echo "------------------------------"
    # 退出信息
    echo -e "Press 'Ctrl+C' to exit"
  done
}
# 判断执行参数
if [[ -n "$1" ]];then
  # 执行函数
  traffic_monitor $1
else
  echo -e "None parameter,please add system netport after run the script! \nExample: 'sh traffic_monitor eth0'"
fi
