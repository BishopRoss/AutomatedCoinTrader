import CryptoAutomation as CA
from coinbase.wallet.client import Client

coinbase_API_key = "Enter your key here"
coinbase_API_secret = "Enter your Secret key here"
client = Client(coinbase_API_key, coinbase_API_secret)

# This coin watcher monitors the ADA coin.
CA.buyMonitorProto("ADA-USD", "ADA", "50", 2.77)
CA.buyMonitorProto("ADA-USD", "ADA", "50", 2.77)
CA.buyMonitorProto("ADA-USD", "ADA", "50", 2.75)
