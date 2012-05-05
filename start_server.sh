#!/bin/bash

dir=/home/ubuntu/git/sensor-server

cd $dir
start-stop-daemon --make-pidfile \
                  --pidfile "/home/ubuntu/server.pid" \
                  -b --startas "$dir/bin/python" -S \
                  -- "$dir/src/server.py"

