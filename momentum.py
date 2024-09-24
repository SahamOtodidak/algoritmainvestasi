import yfinance as yf
import datetime

today = datetime.datetime.now().date()
def momentum_trading(prices, threshold=0.05):
    buy_price = None
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1] * (1 + threshold) and buy_price is None:
            buy_price = prices[i]
            print(f"Beli di harga: {buy_price}")
        elif prices[i] < prices[i-1] * (1 - threshold) and buy_price is not None:
            if prices[i] < buy_price:
                sell_price = prices[i]
                print(f"Jual di harga: {sell_price}")
                buy_price = None

data = yf.download('FDX', start='2024-09-16', end='2024-09-22', interval='5m')

prices = data['Close'].tolist()

momentum_trading(prices, threshold=0.009)
