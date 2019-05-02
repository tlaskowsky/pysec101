#!/usr/bin/python
#-*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import response

@route('/')
def hello():
    response.set_header('X-Frame-Options', 'DENY')
    html = '<h2>Target Website</h2>'
    html += '<button type="button" value="button" '
    html += 'onclick="alert(\'Purchased Product A\')">'
    html += 'Buy Product A</button>'
    return html

run(host='0.0.0.0', port=8000, debug=True)
