# Zerodha_Toolkit 
Toolkit to simplify algo trading using Zerodha's Kite API. If you're new to Zerodha API, this repo provides clear, functional code examples.

## Prerequisites
- Python >= 3.7
- Install packages using: `pip install kite_trade python-dotenv`

## Features Covered
- Request token login: generate access token via Kite login URL (official method)
- Fetch profile, margins, orders, positions
- Retrieve instruments and historical data
- Place, modify, and cancel orders via code

## Login Example
### python
from kite_trade import *
from dotenv import load_dotenv
import os

load_dotenv()
user_id = os.getenv("USER_ID")
password = os.getenv("PASSWORD")
twofa = os.getenv("TWOFA")

enctoken = get_enctoken(user_id, password, twofa)
kite = KiteApp(enctoken=enctoken)

