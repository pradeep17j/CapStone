import yfinance as yf

spy = yf.Ticker("SPY")

spy.info

spy.history(period="max")

# The ability to access options, if needed
spy.option_chain()
