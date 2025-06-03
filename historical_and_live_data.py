## symbol = [// put all stocks name here//]
# Fetch instrument tokens for the symbols
def get_instrument_token(symbol):
    instruments = kite.instruments("NSE")
    for instrument in instruments:
      if instrument['tradingsymbol'] == symbol:
          return instrument['instrument_token']
    return None


 # Get instrument tokens for all symbols
instrument_tokens = {symbol: get_instrument_token(symbol) for symbol in symbols}


# Fetch historical data for a given instrument token
def fetch_historical_data(kite, instrument_token):
    today = datetime.datetime.now()
    from_date = today - datetime.timedelta(days=30)
    try:
        historical = kite.historical_data(
            instrument_token=instrument_token,
            from_date=from_date.strftime("%Y-%m-%d"),
            to_date=today.strftime("%Y-%m-%d"),
            interval="day"
        )
        return pd.DataFrame(historical)
    except Exception as e:
        print(f"Failed to fetch historical data for token {instrument_token}: {e}")
        return pd.DataFrame()


# Function to fetch stock data for multiple symbols
def get_stock_data(kite, symbols):
    stock_data = []
    try:
        # Fetch live data for multiple symbols
        ltp_data = kite.ltp([f"NSE:{symbol}" for symbol in symbols])
        for symbol in symbols:
            ltp = ltp_data[f"NSE:{symbol}"]["last_price"]
            stock_data.append({"symbol": symbol, "price": ltp})
    except Exception as e:
        print(f"Failed to fetch live data for symbols {symbols}: {e}")
    return stock_data
