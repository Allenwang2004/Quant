from binance.client import Client
from config import api_key, api_secert
client = Client(api_key, api_secert)

client.futures_change_margin_type(symbol='ETHUSDT', marginType='ISOLATED')