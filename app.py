from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes, convert
from decimal import Decimal
# from convert import convert
import convert


app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
rates = CurrencyRates()
codes = CurrencyCodes()
# should I be storing rates and codes in the session?
# is it possible to store these in the session outside of a route?
debug = DebugToolbarExtension(app)


@app.route('/')
def show_convert_form():
    """Show the form to input conversion info."""
    return render_template('index.html')


