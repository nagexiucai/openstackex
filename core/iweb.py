#!/usr/bin/env python
#coding=utf-8
#by nagexiucai

from core.dbwrapper import MiniDBMS
from core.fs import FS
import web

db = MiniDBMS()
TEMPLATES = FS.join_path(FS.inner_root(), 'misc', 'templates')
render = web.template.render(TEMPLATES)
urls = (
    '/', 'index'
    )
 
class index:
    def GET(self):
        #todo: howto share sqlite'db between processes
        records = db.show('timestamp') or [('ready', '1479115419.25'), ('ready', '1479115423.56')]
        return render.index(records)

def run():
    app = web.application(urls, globals())
    app.run()

if __name__ == '__main__':
    run()
