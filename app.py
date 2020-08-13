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
debug = DebugToolbarExtension(app)


@app.route('/')
def show_convert_form():
    """Show the form to input conversion info."""
    return render_template('index.html')


@app.route('/convert')
def convert_currency():
    """Convert the amount given into the new currency."""
    from_curr = request.args.get("convert-from").upper()
    to_curr = request.args.get("convert-to").upper()
    amount = request.args.get("amount")

    session['from_curr'] = from_curr
    session['to_curr'] = to_curr
    session['amount'] = amount

    try:
        result = convert(from_curr, to_curr, amount)
        session['symbol'] = result["symbol"]
        raw_conversion = result["raw_conversion"]

        return redirect('/conversion-result')
        # is it possible to send variables on a redirect?

    except:
        if codes.get_symbol(from_curr) == None:
            flash(f"Not a valid currency: {from_curr}", "error")
        if codes.get_symbol(to_curr) == None:
            flash(f"Not a valid currency: {to_curr}", "error")
        if float(amount) < 0:
            flash(f"Not a valid amount.", "error")
        return redirect('/')


