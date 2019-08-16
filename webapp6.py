# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:26:10 2019

@author: HP
"""

from flask_table import Table, Col
from flask import Flask
from io import BytesIO
from flask import Flask, render_template, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')

app = Flask(__name__)


class ItemTable(Table):
    recordTime = Col('recordTime')
    recordValue = Col('recordValue')
    
@app.route('/')
def data_frame_visualization():
    fig, ax = plt.subplots()
    df= realdf
    time=df['time']
    gasprice=df['cvalue']
    plt.plot(time,gasprice, color='orange')
    plt.xlabel("Time (Year)")
    plt.ylabel("Gas Price")
    plt.title("Time Series of US Gasoline Prices ")
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    items = Item.get_elements()
    table = ItemTable(items)

    # You would usually want to pass this out to a template with
    # render_template.
    
    
    return  '{} {}'.format(send_file(img, mimetype='image/png'))
"""

@app.route('/')
def index():
    items = Item.get_elements()
    table = ItemTable(items)

    # You would usually want to pass this out to a template with
    # render_template.
    return table.__html__()
"""
class Item(object):
    """ a little fake database """
    def __init__(self,recordTime, recordValue):
        self.recordTime = recordTime
        self.recordValue = recordValue

    @classmethod
    def get_elements(cls):
        return anlist

if __name__ == '__main__':
    app.run()