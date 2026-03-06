import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
CMC_KEY = os.getenv("CMC_KEY")

SYMBOL_DEFAULT = "BTC"
