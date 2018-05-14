#!/bin/bash 
function aircon {
    :
}
if [ "$TOPIC" == "iot-2/cmd/switch/fmt/text" ];then
	echo  1>&2
	echo 1>&2 "set state of switch to $PAYLOAD"
	echo  1>&2

	#pilight-control -d "switch2" -s $PAYLOAD
	[ "$PAYLOAD" == "on" ] && arg="-o4"
	[ "$PAYLOAD" == "off" ] && arg="-f4"
	[ "$arg" != "" ] && echo  $arg
else
	echo  1>&2
	echo "not my topic $TOPIC"
	echo  1>&2
fi
