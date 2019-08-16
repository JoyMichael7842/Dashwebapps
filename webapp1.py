# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:20:13 2019

@author: HP
"""

from flask import Flask,render_template, request
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route("/")
def index():
	return "hello"
if __name__ == "__main__":
    app.run()