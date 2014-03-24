#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import web
from src.controller import sinatest

render = web.template.render('templates/', base='layout')
render_without_layout = web.template.render('templates/')

urls = (
#    '/api/app', AppController.app_app,
#    '/api/status', StatusController.app_status,
    '/api/sina',sinatest.sina_test,
    '/(status/?)?', 'status',
    '/chart/?', 'chart',
    '/data/(.*)', 'data',
    '/log/(.*)', 'log',
    '/test/', 'test',
)

class home:
    def GET(self,name):
        return render.home()

class status:
    def GET(self,name):
        return render.status()

class chart:
    def GET(self):
        return render.chart()

class data:
    def GET(self, data):
        return render.data(data)

class log:
    def GET(self,platform):
        data=[platform]
        return render.log(platform)

class test:
    def GET(self):
        return render.test()



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()