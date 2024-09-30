import backtrader as bt
import datetime
import yfinance as yf

today = datetime.datetime.now().date()
data = bt.feeds.PandasData(dataname=yf.download('FDX', start='2024-08-01', end=today, interval='1d'))

class MomentumStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.momentum = bt.indicators.Momentum(self.dataclose, period=10)
        self.sma = bt.indicators.SimpleMovingAverage(self.dataclose, period=20)

    def next(self):
        print(f'Momentum: {self.momentum[0]}, Price : {self.dataclose[0]}')
        if self.momentum[0] > 70 and self.dataclose[0] > self.sma[0]: # Momentum naik
            self.buy()
            print(f'Beli di {self.dataclose[0]}')
        elif self.momentum[0] < 30 and self.dataclose[0] > self.sma[0]: # Momentum turun
            self.sell()
            print(f'Jual di {self.dataclose[0]}')

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(MomentumStrategy)
cerebro.run()
cerebro.plot()
