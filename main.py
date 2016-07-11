# -*- coding: utf-8 -*-
# @Date    : 2016-05-19 17:45
# @Author  : max

from sqlalchemy.orm import scoped_session, sessionmaker
from mod.models.db import engine
from mod.classTable.handler import ClassHandler
from mod.tuling.handler import TulingHandler
from mod.schoolbus.handler import SchoolBusHandler
import tornado.web
import tornado.ioloop
import tornado.options


from tornado.options import define, options
define('port', default=7005, help='run on the given port', type=int)


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/wechat/class', ClassHandler),
            (r'/wechat/tuling',TulingHandler),
            (r'/wechat/schoolbus',SchoolBusHandler)
        ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))

if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(options.port, address='127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()
