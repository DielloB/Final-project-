import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_exchange_rate(base_currency, target_currency):
    """Fetch the exchange rate between two currencies."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency, None)

def convert_currency(amount, base_currency, target_currency):
    """Convert an amount from one currency to another."""
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is None:
        return None
    return round(amount * rate, 2)

@app.route('/', methods=['GET', 'POST'])
def main():
    """Handles the UI for the currency converter."""
    result = None
    error = None
    currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD"]

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']

            if from_currency not in currencies or to_currency not in currencies:
                error = "Unsupported currency."
            else:
                result = convert_currency(amount, from_currency, to_currency)
                if result is None:
                    error = "Conversion rate unavailable."
        except ValueError:
            error = "Please enter a valid amount."

    return render_template('index.html', result=result, error=error, currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
