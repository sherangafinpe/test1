# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:59:42 2021

@author: Sheranga
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

