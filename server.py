# -*- coding: utf-8 -*-
'''
Created on 2016-1-28

@author: yaoyf
'''


import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web

class LogHandler(tornado.web.RequestHandler):
    def post(self):
        req = self.request.body
        print req
    
    
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

            
if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application([
                    (r'/log',LogHandler)
                    ])
    http_server = tornado.httpserver.HTTPServer(application)
    '''
    ##multi-process
    http_server.bind(options.port)
    http_server.start(4)
    '''
    ##single-process
    http_server.listen(options.port)
    
    tornado.ioloop.IOLoop.instance().start()
    #os.system('python server.py -logging=info -log_file_prefix=./log/api.log') 