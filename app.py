from flask import Flask, jsonify, render_template, request, url_for
import yfinance as yf
import backtrader as bt
import random

app = Flask(__name__)

# Define the SuperTrend indicator
class SuperTrend(bt.Indicator):
    lines = ('supertrend',)
    params = (('period', 10), ('multiplier', 3),)

    def __init__(self):
        self.addminperiod(self.params.period)
        atr = bt.indicators.ATR(self.data, period=self.params.period)
        hl2 = (self.data.high + self.data.low) / 2
        self.l.up = hl2 - (self.params.multiplier * atr)
        self.l.dn = hl2 + (self.params.multiplier * atr)
        self.l.supertrend = bt.If(self.data.close > self.l.dn, self.l.up, self.l.dn)

# Strategy for trading
class TradingStrategy(bt.Strategy):
    params = (
        ('ema_period', 15),
        ('vwap_period', 14),
        ('supertrend_period', 10),
        ('supertrend_multiplier', 3),
        ('stop_loss', 0.95),
    )

    def __init__(self):
        self.ema = bt.indicators.EMA(self.data, period=self.params.ema_period)
        self.vwap = bt.indicators.VolumeWeightedAveragePrice(self.data)
        self.supertrend = SuperTrend(self.data, period=self.params.supertrend_period, multiplier=self.params.supertrend_multiplier)
        self.order = None
        self.buy_price = None
        self.stop_price = None

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.data.close > self.ema and self.data.close > self.vwap:
                self.order = self.buy()
                self.buy_price = self.data.close[0]
                self.stop_price = self.buy_price * self.params.stop_loss
        else:
            if self.data.close < self.stop_price:
                self.order = self.sell()

    def notify_order(self, order):
        if order.status in [order.Completed, order.Canceled, order.Margin]:
            self.order = None

    def stop(self):
        pnl = self.broker.get_value() - 10000
        print(f'Final PnL: {pnl}')

# Fetch historical data
def fetch_data(ticker):
    data = yf.download(ticker, start='2022-01-01', end='2023-01-01')
    data.reset_index(inplace=True)
    data['Date'] = data['Date'].astype(str)
    return data

# Route to serve the trading dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Route to get historical data
@app.route('/get_data', methods=['GET'])
def get_data():
    ticker = request.args.get('ticker', 'AAPL')
    data = fetch_data(ticker)
    return data.to_json(orient='records')

# Route to execute a trade
@app.route('/trade', methods=['POST'])
def trade():
    trade_data = request.get_json()
    return jsonify({"status": "success", "data": trade_data})

# Route to get the image path
@app.route('/get_image', methods=['GET'])
def get_image():
    ticker = request.args.get('ticker', 'AAPL')
    image_path = get_image_path(ticker)
    return jsonify({"image_path": image_path})

def get_image_path(ticker):
    # Define image paths for each ticker
    image_paths = {
        'AAPL': url_for('static', filename='images/apple.png'),
        'MSFT': url_for('static', filename='images/microsoft.png'),
        'GOOGL': url_for('static', filename='images/google.png'),
        'AMZN': url_for('static', filename='images/amazon.png'),
        'TSLA': url_for('static', filename='images/tesla.png'),
    }
    default_image_path = url_for('static', filename='images/placeholder.png')  # Placeholder or default image
    return image_paths.get(ticker, default_image_path)

@app.route('/get_additional_data', methods=['GET'])
def get_additional_data():
    # Generate dummy data for demonstration
    data = {
        'bullish_scenario': round(random.uniform(40, 60), 2),
        'bearish_scenario': round(random.uniform(40, 60), 2),
        'net_profit_loss': round(random.uniform(-10, 10), 2),
        'volume': random.randint(1_000_000, 10_000_000),
        'suggestion': random.choice(['Long', 'Short'])
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
