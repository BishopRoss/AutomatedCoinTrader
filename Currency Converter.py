import CryptoAutomation as CA

coinbase_API_key = "Enter your key here"
coinbase_API_secret = "Enter your secret key here"
client = CA.Client(coinbase_API_key, coinbase_API_secret)

currencies = client.get_currencies()
print(currencies)
rates = client.get_exchange_rates(currency = "USD")

