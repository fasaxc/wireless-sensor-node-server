# Copyright (c)Shaun Crampton 2012-2012. All rights reserved.

import time

import tornado
import cjson

from data import Session, Reading
import datetime

class ReadingsHandler(tornado.web.RequestHandler):
    def get(self):
        sess = Session()

        self.set_header("Content-Type", "application/json")

        self.write('{"num_nodes":2,"readings":[')
        i = 0
        last_timestamp = {}
        now = datetime.datetime.utcnow()
        one_month_ago = now - datetime.timedelta(days=30)
        one_week_ago = now - datetime.timedelta(days=7)
        one_day_ago = now - datetime.timedelta(days=1)
        for r in (sess.query(Reading).
                       filter(Reading.checksum_calc == Reading.checksum_sent).
                       order_by(Reading.created_at)):
            if r.created_at < one_month_ago:
                min_delta = datetime.timedelta(hours=2)
            elif r.created_at < one_week_ago:
                min_delta = datetime.timedelta(hours=1)
            elif r.created_at < one_day_ago:
                min_delta = datetime.timedelta(minutes=40)
            else:
                min_delta = datetime.timedelta()
            if (last_timestamp.get(r.node_id, None) is None or
                r.created_at > last_timestamp[r.node_id] + min_delta):
                self.write(("" if i == 0 else ",") +
                       cjson.encode([time.mktime(r.created_at.timetuple()),
                                     r.reading if r.node_id == 1 else None,
                                     r.reading if r.node_id == 2 else None,
                                     r.reading if r.node_id == 3 else None]))
                last_timestamp[r.node_id] = r.created_at
            i += 1
            if (i % 20) == 0:
                self.flush()

        self.finish("]}")
