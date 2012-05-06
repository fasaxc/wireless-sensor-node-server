# Copyright (c)Shaun Crampton 2012-2012. All rights reserved.

import time

import tornado
import cjson

from data import Session, Reading

class ReadingsHandler(tornado.web.RequestHandler):
    def get(self):
        sess = Session()

        self.set_header("Content-Type", "application/json")

        self.write('{"num_nodes":2,"readings":[')
        i = 0
        for r in sess.query(Reading).order_by(Reading.created_at):
            self.write(("" if i == 0 else ",") +
                       cjson.encode([time.mktime(r.created_at.timetuple()),
                                     r.reading if r.node_id == 1 else None,
                                     r.reading if r.node_id == 2 else None]))
            i += 1
            if (i % 20) == 0:
                self.flush()

        self.finish("]}")
