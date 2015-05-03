import time
import cjson
import datetime

import tornado.web
import settings
import tornado
from data import Session, Reading


class ReadingsHandler(tornado.web.RequestHandler):
    def get(self):
        sess = Session()

        self.set_header("Content-Type", "application/json")

        self.write('{"num_nodes":3,"readings":[')
        i = 0
        last_timestamp = {}
        now = datetime.datetime.utcnow()
        one_month_ago = now - datetime.timedelta(days=30)
        one_year_ago = now - datetime.timedelta(days=365)
        one_week_ago = now - datetime.timedelta(days=7)
        one_day_ago = now - datetime.timedelta(days=1)
        for r in (sess.query(Reading).
                      filter(Reading.checksum_calc == Reading.checksum_sent).
                      filter(Reading.created_at > one_year_ago).
                      order_by(Reading.created_at)):
            if r.created_at < one_month_ago:
                min_delta = datetime.timedelta(hours=4)
            elif r.created_at < one_week_ago:
                min_delta = datetime.timedelta(hours=2)
            elif r.created_at < one_day_ago:
                min_delta = datetime.timedelta(hours=1)
            else:
                min_delta = datetime.timedelta()
            if (last_timestamp.get(r.node_id, None) is None or
                r.created_at > last_timestamp[r.node_id] + min_delta):
                self.write(("" if i == 0 else ",") +
                       cjson.encode([time.mktime(r.created_at.timetuple()), #@UndefinedVariable
                                     r.reading if r.node_id == 1 else None,
                                     r.reading if r.node_id == 2 else None,
                                     r.reading if r.node_id == 3 else None]))
                last_timestamp[r.node_id] = r.created_at
            i += 1
            if (i % 20) == 0:
                self.flush()

        self.finish("]}")


URLS = [
    (r'^/readings/?$', ReadingsHandler),
    ("^/(.*)$", tornado.web.StaticFileHandler, {"path": settings.STATIC_DIR,
                                                "default_filename": "index.html"}),
]
