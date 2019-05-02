#!/usr/bin/python
#-*- coding: utf-8 -*-

from bottle import route
from bottle import run
from bottle import request
from bottle import redirect
from bottle import response
import sqlite3

db_name = 'tasklist.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

@route('/')
def hello(user=''):
    tasks = get_tasklist()
    
    html = "<h2>Persistent XSS Demo</h2>"
    html += "<form action='./' method='POST'>"
    html += "Task name: <input type='text' name='name' /><br>"
    html += "Details: <input type='text' name='detail' /><br>"
    html += "<input type='submit' name='register' value='Register'/>"
    html += "</form>"
    html += tasks
    
    response.set_header('X-XSS-Protection', '1; mode=block')
    response.set_header('Content-Security-Policy', "default-src 'self'")
    
    return html

@route('/', method='POST')
def register():
    name = request.forms.get('name')
    detail = request.forms.get('detail')
    
    sql_query = 'INSERT INTO tasklist values(?, ?)'
    cursor.execute(sql_query, (name, detail))
    conn.commit()
    
    return redirect('/')

def get_tasklist():
    sql_query = 'SELECT * FROM tasklist'
    result = cursor.execute(sql_query)
    
    html = '<table border="1">'
    for row in result:
        html += '<tr><td>'
        html += row[0].encode('utf-8')
        html += '</td><td>'
        html += row[1].encode('utf-8')
        html += '</td></tr>'

    html += '</table>'
    return html

run(host='0.0.0.0', port=8080, debug=True)
