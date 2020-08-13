from flask import request
from unittest import TestCase
from app import app
from convert import convert


app.config['TESTING'] = True
# how does the following work?
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ConvertCurrencyTestCase(TestCase):
    """Unit tests on forex-python currency conversion"""

    def test_show_convert_form(self):
