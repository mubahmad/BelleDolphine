#!/bin/bash

sudo nmcli device wifi hotspot ssid dolphin password 12344321 ifname wlan0
/usr/bin/python3 ./flask_app/app.py &> /dev/null
/usr/bin/python3 ./main.py &> /dev/null
