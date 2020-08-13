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
        """Test"""
        with app.test_client() as client:
            res = client.get('/')

            self.assertEqual(res.status_code, 200)

    def test_show_convert_form_submit(self):
        """Test"""

        with app.test_client() as client:
            # res = client.get('/')
            res = client.get(
                '/', query_string={'convert-from': 'usd', 'convert-to': 'sek', 'amount': '1'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            # check the query values
            self.assertEqual(request.args['convert-from'], 'usd')
            self.assertEqual(request.args['convert-to'], 'sek')
            self.assertEqual(request.args['amount'], '1')
            # check that the correct page is rendered
            self.assertIn('<h1>Forex Converter</h1>', html)

    def test_convert_currency(self):
        """Test"""

        with app.test_client() as client:
            res = client.get(
                '/convert', query_string={'convert-from': 'ron', 'convert-to': 'ron', 'amount': '1'})
            self.assertEqual(request.args['convert-from'], 'ron')
            self.assertEqual(request.args['convert-to'], 'ron')
            self.assertEqual(res.status_code, 302)
            self.assertEqual(
                res.location, "http://localhost/conversion-result")

