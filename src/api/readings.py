# Copyright (c) Metaswitch Networks 2012-2012. All rights reserved.

import time

import tornado

from data import Session, Reading

class ReadingsHandler(tornado.web.RequestHandler):
    def get(self):
        sess = Session()
        result = []
        for r in sess.query(Reading).order_by(Reading.created_at):
            result.append([time.mktime(r.created_at.timetuple()), r.reading])
        self.finish({"readings": result})
