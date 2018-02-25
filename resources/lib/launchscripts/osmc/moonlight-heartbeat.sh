#!/usr/bin/env bash

POST_SCRIPT=$1

killall -STOP kodi.bin

sleep 10

while [ true ]; do
        status="$(pidof moonlight | wc -w)"
        if [ ${status} -ne 1 ]; then
            if [ ${POST_SCRIPT} != "" ]; then
                ${POST_SCRIPT}
            fi

            killall -CONT kodi.bin
            exit
        else
            sleep 2
        fi
done
