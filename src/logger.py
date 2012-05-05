#!/usr/bin/env python

import logging
import time

import serial

from data import Session, Reading

log = logging.getLogger()

def standalone():
    db = Session()
    while True:
        try:
            log.info("Opening serial port")
            ser = serial.Serial('/dev/ttyACM0', 115200, timeout=10)
            log.info("Serial port open")

            while True:
                line = ser.readline()
                if line:
                    (node_id, seq_no, reading_type, reading,
                     checksum_sent, checksum_calc) = line.split(" ")
                    r = Reading()
                    r.node_id = int(node_id)
                    r.seq_no = int(seq_no)
                    r.reading_type = reading_type
                    r.reading = float(reading)
                    r.checksum_sent = int(checksum_sent, 16)
                    r.checksum_calc = int(checksum_calc, 16)
                    db.add(r)
                    db.commit();
                    log.info("Read line: %r", line)
        except Exception:
            log.exception("Exception")
            time.sleep(20)


if __name__ == '__main__':
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)
    handler = logging.FileHandler("/tmp/sensor-logger.log")
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    standalone()
