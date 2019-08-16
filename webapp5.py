# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:58:07 2019

@author: HP
"""

from io import BytesIO
from flask import Flask, render_template, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 
 
app = Flask(__name__)
 


 

 
@app.route('/data_frame_visualization/')
def data_frame_visualization():
    fig, ax = plt.subplots()
    df=realdf
    time=df['time']
    gasprice=df['cvalue']
    plt.plot(time,gasprice, color='orange')
    plt.xlabel("Time (Year)")
    plt.ylabel("Gas Price")
    plt.title("Time Series of US Gasoline Prices ")
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
 
@app.route('/data_frame_analysis')
def data_frame_analysis():
    return '{} {}'.format(render_template("data_frame_analysis.html"),"hello world")
#render_template("data_frame_analysis.html")



if __name__ == '__main__':
    app.run()