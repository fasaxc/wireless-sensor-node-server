#!/bin/bash

dir=/home/ubuntu/git/sensor-server

cd $dir
start-stop-daemon --make-pidfile \
                  --pidfile "/home/ubuntu/logger.pid" \
                  -b --startas "$dir/bin/python" -S \
                  -- "$dir/src/logger.py"

