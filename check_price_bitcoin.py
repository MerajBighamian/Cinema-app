#get number of price Bitcoin
import requests

response = requests.get('https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD')

price = response.json()

print(price['high'])
