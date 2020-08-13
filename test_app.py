from flask import request
from unittest import TestCase
from app import app
from convert import convert


app.config['TESTING'] = True
# how does the following work?
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


