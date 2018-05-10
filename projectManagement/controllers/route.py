# -*- coding: utf-8 -*-
# from [projectname] dari var yang sudah dideclare di init.py
from projectManagement import app
# flask adalah web server
from flask import render_template

from projectManagement.models.auth import signin



@app.route('/')
def start():
    return render_template('base/index.html')

@app.route('/opo')
def opo():
    return render_template('blue/index.html')


