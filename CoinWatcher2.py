import CryptoAutomation as CA
from coinbase.wallet.client import Client

coinbase_API_key = "Enter your key here"
coinbase_API_secret = "Enter your secret key here"
client = Client(coinbase_API_key, coinbase_API_secret)

# This is my coin watcher for ADA
# Smart DCA test. This will execute three buy orders for
# $92.00 when ADA drops to 2.75, 2.73, and 2.71
CA.buyMonitorProto("ADA-USD", "ADA", "92.00", 2.75)
CA.buyMonitorProto("ADA-USD", "ADA", "92.00", 2.73)
CA.buyMonitorProto("ADA-USD", "ADA", "92.00", 2.71)




