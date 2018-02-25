#!/bin/sh
# Originally written by miko
# Modified by dodslaser
# Modified again by wackerl91 (support for launch args)

LAUNCHER_PATH=$1
HEARTBEAT_PATH=$2
HOST=$3
KEY_DIR=$4
GAME=$5
CONF_PATH=$6
DEBUG_ENABLED=$7
PRE_SCRIPT=$8
POST_SCRIPT=$9

if [ ${PRE_SCRIPT} != "" ]; then
    ${PRE_SCRIPT} \"${HOST}\" \"${GAME}\"
fi

$HEARTBEAT_PATH ${POST_SCRIPT} &

$LAUNCHER_PATH "${HOST}" "${GAME}" $CONF_PATH ${KEY_DIR} $DEBUG_ENABLED >/dev/null 2>&1 &

sleep 2

exit
