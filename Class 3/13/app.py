from flask import Flask, render_template, request

app = Flask(__name__)

# Mock stock database
STOCKS = {
    "AAPL": {"name": "Apple Inc.", "price": 182.52, "change": "+1.25%", "market_cap": "2.83T", "pe_ratio": "29.4"},
    "TSLA": {"name": "Tesla, Inc.", "price": 175.34, "change": "-2.10%", "market_cap": "558.2B", "pe_ratio": "42.1"},
    "GOOGL": {"name": "Alphabet Inc.", "price": 142.65, "change": "+0.85%", "market_cap": "1.78T", "pe_ratio": "26.8"},
    "MSFT": {"name": "Microsoft Corporation", "price": 415.50, "change": "+1.12%", "market_cap": "3.09T", "pe_ratio": "36.5"},
    "AMZN": {"name": "Amazon.com, Inc.", "price": 178.75, "change": "-0.45%", "market_cap": "1.86T", "pe_ratio": "60.2"}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    searched_ticker = None
    error = None

    if request.method == 'POST':
        searched_ticker = request.form.get('ticker', '').upper().strip()
        if searched_ticker in STOCKS:
            stock_data = STOCKS[searched_ticker]
        else:
            error = f"Ticker symbol '{searched_ticker}' not found. Try AAPL, TSLA, GOOGL, MSFT, or AMZN."

    return render_template('index.html', stock=stock_data, ticker=searched_ticker, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5001)