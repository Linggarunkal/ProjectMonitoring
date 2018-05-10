# -*- coding: utf-8 -*-
# from [projectname] dari var yang sudah dideclare di init.py
from projectManagement import app
# flask adalah web server
from flask import render_template



@app.route('/')
def start():

    parsing = "tempe"
    return render_template('content/home.html', parsing=parsing)

@app.route('/opo')
def opo():
    return render_template('base/header.html')


