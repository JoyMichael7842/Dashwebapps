# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:40:42 2019

@author: HP
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'