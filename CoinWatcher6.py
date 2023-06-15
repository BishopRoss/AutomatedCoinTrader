import CryptoAutomation as CA
from coinbase.wallet.client import Client

coinbase_API_key = "Enter your key here"
coinbase_API_secret = "Enter your secret key here"
client = Client(coinbase_API_key, coinbase_API_secret)

# This coin watcher monitors the ADA coin.
#CA.buyMonitorProto("ACH-USD", "ACH", "400", 0.12)
print("ACH Coin has been bought, now watching it to sell.")
CA.coinSellMonitor("ACH", "ACH-USD", 0.15)
