import yfinance as yf


def get_stock_data(stock_id):
    stock = yf.Ticker(f"{stock_id}.TW")
    data = stock.history(period="5d")
    return data