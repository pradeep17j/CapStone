import yfinance as yf

spy = yf.Ticker("SPY")

spy.info

spy.history(period="max")

# The ability to access options, if needed
spy.option_chain()

data = yf.download("SPY", start="2020-01-01", end="2020-12-31")