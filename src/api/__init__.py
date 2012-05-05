import tornado.web

from api import readings

import settings

URLS = [
    (r'^/readings/?$', readings.ReadingsHandler),
    ("^/(.*)$", tornado.web.StaticFileHandler, {"path": settings.STATIC_DIR,
                                                "default_filename": "index.html"}),
]
