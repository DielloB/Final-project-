import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_exchange_rate(base_currency, target_currency):
    """Récupère le taux de change entre deux devises."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency, None)

def convert_currency(amount, base_currency, target_currency):
    """Convertit un montant d'une devise à une autre."""
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is None:
        return None
    return round(amount * rate, 2)

def validate_currency(currency, valid_currencies):
    """Vérifie si la devise donnée est valide."""
    return currency in valid_currencies

@app.route('/', methods=['GET', 'POST'])
def main():
    """Gère l'interface utilisateur du convertisseur de devises."""
    result = None
    error = None
    currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD"]  # Exemple, peut être étendu
    
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']

            if not validate_currency(from_currency, currencies) or not validate_currency(to_currency, currencies):
                error = "Devise non prise en charge."
            else:
                result = convert_currency(amount, from_currency, to_currency)
                if result is None:
                    error = "Taux de conversion non disponible."
        except ValueError:
            error = "Veuillez entrer un montant valide."

    return render_template('index.html', result=result, error=error, currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
