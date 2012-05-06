# Copyright (c)Shaun Crampton 2012-2012. All rights reserved.

import time

import tornado

from data import Session, Reading

class ReadingsHandler(tornado.web.RequestHandler):
    def get(self):
        sess = Session()
        result = []
        for r in sess.query(Reading).order_by(Reading.created_at):
            result.append([time.mktime(r.created_at.timetuple()),
                           r.reading if r.node_id == 1 else None,
                           r.reading if r.node_id == 2 else None])
        self.finish({"num_nodes": 2,
                     "readings": result})
