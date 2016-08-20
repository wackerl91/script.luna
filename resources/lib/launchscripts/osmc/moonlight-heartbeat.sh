#!/usr/bin/env bash

killall -STOP kodi.bin

sleep 10

while [ true ]; do
        status="$(pidof moonlight | wc -w)"
        if [ ${status} -ne 1 ]; then
            killall -CONT kodi.bin
            exit
        else
            sleep 2
        fi
done
