# -*- coding: utf-8 -*-
__version__ = '0.1'
# flask adalah web server
from flask import Flask
import os

app = Flask('projectManagement')
app.config['SECRET_KEY'] = os.urandom(24)
app.config['ALLOWED_EXTENSIONS'] = ['pdf']
app.config['UPLOAD_FOLDER'] = 'projectManagement/static/document'
app.debug = True

from projectManagement.controllers import *
