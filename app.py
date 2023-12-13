from flask import Flask, render_template, request

app = Flask(__name__)


class Currency:

    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return f'<Currency {self.code}>'


class CantorOffer:
    def __init__(self):
        self.currencies = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dollar', 'flag_usa.png'))
        self.currencies.append(Currency('EUR', 'Euro', 'flag_euro.png'))
        self.currencies.append(Currency('JPY', 'Yen', 'flag_japan.png'))
        self.currencies.append(Currency('GPB', 'Pound', 'flag_uk.png'))

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknown', 'unknown', 'flag_pirat.png')


@app.route("/")
def index():
    return "This is index"


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()
    offer.load_offer()

    if request.method == 'GET':
        return render_template('exchange.html', offer=offer)
    else:
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']

        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']

        return render_template('exchange_results.html', currency=currency, amount=amount)


if __name__ == '__main__':
    app.run(debug=True)
