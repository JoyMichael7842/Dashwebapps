# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:29:39 2019

@author: HP
"""

from flask_table import Table, Col
from flask import Flask

app = Flask(__name__)

class ItemTable(Table):
    recordTime = Col('recordTime')
    recordValue = Col('recordValue')
    
@app.route('/')
def index():
    items = Item.get_elements()
    table = ItemTable(items)

    # You would usually want to pass this out to a template with
    # render_template.
    return table.__html__()

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