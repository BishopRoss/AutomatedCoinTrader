import CryptoAutomation as CA
from coinbase.wallet.client import Client

coinbase_API_key = "Enter your Key here"
coinbase_API_secret = "Enter your secret Key here"
client = Client(coinbase_API_key, coinbase_API_secret)

CA.buyMonitorProto("ACH-USD", "ACH", "100.01", 0.09)
