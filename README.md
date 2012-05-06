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
  
I use Monit to monitor and start the server and iptables to redirect port 80
to port 8888, where the tornado server runs.  (This allows running the server as
a non-root user.)

Setup
=====

On Ubuntu, do this:

* sudo apt-get install git-core python python-dbg python-dev python-virtualenv 
  ubuntu-dev-tools monit sqlite3 iptables-persistent python2.6-dev
* as root, edit /etc/monit/monitrc, add lines "set daemon 10" and "include /etc/monit/conf.d/*"
* as root copy the file monitrc into /etc/monit/conf.d
* as root, edit /etc/defaults/monit and set the start variable to 1.
* edit the start/stop_server/logger.sh scripts to match the paths that you used
  for your repo.
* from the root of the repo, run "make env" to create a python virtual env with
  all the right dependencies in it
* run sudo /etc/init.d/monit start

Connect to http://<your server>:8888