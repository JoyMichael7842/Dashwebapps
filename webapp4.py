# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:50:26 2019

@author: HP
"""

from flask import Flask, render_template
from graph import build_graph
 
app = Flask(__name__)
 
@app.route('/')
def graphs():
    #These coordinates could be stored in DB
    x1 = [0, 1, 2, 3, 4]
    y1 = [10, 30, 40, 5, 50]
    
 
    graph1_url = build_graph(x1,y1);
   
 
    return render_template('graphs.html',graph1=graph1_url)
 
if __name__ == '__main__':
    app.run()