#!/usr/bin/python
# interpret the command ("on" or "off") in env var PAYLOAD and calls the script which runs the command against senseHAT

import os

topic=os.getenv("TOPIC")
cmd=os.getenv("PAYLOAD")

if topic == "iot-2/cmd/switch/fmt/text":
	print "\nRunning command ' switch", cmd, "'\n"
	if cmd == "on":
		os.system("btclient.d/text-scroll.py")
	elif cmd == "off":
		os.system("btclient.d/switch-off.py")
	else: 
		print "Error - Command unknown: ", cmd
else:
	print "Error - Topic unknown ", topic
