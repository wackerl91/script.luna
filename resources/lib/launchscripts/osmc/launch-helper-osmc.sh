#!/bin/sh
# Originally written by miko
# Modified by dodslaser
# Modified again by wackerl91 (support for launch args)

LAUNCHER_PATH=$1
HEARTBEAT_PATH=$2
GAME=$3
CONF_PATH=$4
DEBUG_ENABLED=$5

$HEARTBEAT_PATH &

$LAUNCHER_PATH "${GAME}" $CONF_PATH $DEBUG_ENABLED >/dev/null 2>&1 &

sleep 2

exit
