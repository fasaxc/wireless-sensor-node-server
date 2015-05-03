Sensor node server
==================

This project contains the server I use to monitor my wireless sensor network.
It won't do much without a wireless sensor network connected via Arduino to
your serial port!

There are three components:

* in src/logger.py is a python app that reads readings from the serial port
* in src/server.py is a tornado application that serves up the logged data
  over http on port 8888 along with
* the UI, in src/static, which is a JavaScript app that uses Google's chart 
  API to display the data.
  
There are sample upstart job config files in the upstart directory.

To install:
==========

cd wireless-sensor-node-server
sudo pip install .

# If using upstart...
sudo cp upstart/* /etc/init
sudo start wireless-sensor-logger
sudo start wireless-sensor-server

Connect to http://<your server>:8888