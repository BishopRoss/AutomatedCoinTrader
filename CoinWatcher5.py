import CryptoAutomation as CA
from coinbase.wallet.client import Client

coinbase_API_key = "Enter your key here"
coinbase_API_secret = "Enter your secret key here"
client = Client(coinbase_API_key, coinbase_API_secret)

# This coin watcher monitors the REQ coin
CA.buyMonitorProto("REQ-USD", "REQ", "300", 0.20)

# Buy this coin at $0.20, and sell it at $0.35 for a 75% gain.
# Buy this coin at $0.20, and sell it at $0.24 for a 20% gain.
