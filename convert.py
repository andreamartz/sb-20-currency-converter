from forex_python.converter import CurrencyRates, CurrencyCodes, convert

rates = CurrencyRates()
codes = CurrencyCodes()


def convert(from_curr, to_curr, amount):
    """Converts amounts between currencies.

        >>> convert('usd', 'usd', '1')
        1
    """

    raw_conversion = rates.convert(from_curr, to_curr, float(amount))
    symbol = codes.get_symbol(to_curr)
    return {"symbol": symbol, "raw_conversion": raw_conversion}
