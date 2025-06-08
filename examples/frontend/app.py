from flask import Flask, render_template, jsonify
import twstock

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/price/<code>')
def price(code):
    data = twstock.realtime.get(code)
    if data.get('success'):
        return jsonify({'price': data['realtime']['latest_trade_price']})
    return jsonify({'error': data.get('rtmessage', 'fetch error')}), 400

@app.route('/api/candlestick/<code>')
def candlestick(code):
    stock = twstock.Stock(code)
    stock.fetch_31()
    result = [
        {
            't': d.date.strftime('%Y-%m-%d'),
            'o': d.open,
            'h': d.high,
            'l': d.low,
            'c': d.close,
        }
        for d in stock.data
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
