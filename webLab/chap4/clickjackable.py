#!/usr/bin/python
#-*- coding: utf-8 -*-

from bottle import route
from bottle import run

@route('/')
def hello():
    html = '<h2>Target Website</h2>'
    html += '<button type="button" value="button" '
    html += 'onclick="alert(\'Bought product A\')">'
    html += 'Purchase product A</button>'
    return html

run(host='0.0.0.0', port=8000, debug=True)
