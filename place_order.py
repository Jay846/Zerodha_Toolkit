# Function to place orders for Zerodha
def place_order(symbol, qty, transaction_type, order_type="MARKET", product="CNC", price=None):
    try:
        if transaction_type == kite.TRANSACTION_TYPE_SELL:
            product = "MIS"  # Always use MIS for shorting
        elif transaction_type == kite.TRANSACTION_TYPE_BUY:
            product = "CNC"  # Use CNC for long buy positions

        order = kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange=kite.EXCHANGE_NSE,
            tradingsymbol=symbol,
            transaction_type=transaction_type,
            quantity=qty,
            product=product,
            order_type=order_type,
            price=price
        )
        print(f"Order placed: {order}")
    except Exception as e:
        print(f"Order placement failed: {e}")
