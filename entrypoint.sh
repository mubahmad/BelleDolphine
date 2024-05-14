#!/bin/bash

sudo nmcli device wifi hotspot ssid dolphin password 12344321 ifname wlan0
echo problem1
sudo /usr/bin/python3 ./flask_app/app.py &>> /tmp/flask.log
echo problem2
/usr/bin/python3 ./main.py &>> /tmp/dolphin.log
echo problem3
