# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:01:34 2019

@author: HP
"""

from io import BytesIO
from flask import Flask, render_template, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
    items = Item.get_elements()
    table = ItemTable(items)

    return '{} {}'.format(table.__html__(),render_template("data_frame_analysis.html"))
#render_template("data_frame_analysis.html")

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