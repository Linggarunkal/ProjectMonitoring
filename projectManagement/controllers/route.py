# -*- coding: utf-8 -*-
from projectManagement import app
from flask import render_template


@app.route('/')
def start():
    return render_template('base/index.html')
