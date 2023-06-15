# import random
# for i in range(0,500):
#    n = random.randint(1,28)
#   print(n)
import CryptoAutomation as CA
from cbpro.public_client import PublicClient
# CA.accountInfo("ACH")
# CA.emailerForList()
# client = PublicClient()
# tick = client.get_product_ticker("IOTX-USD")
# volume = tick.get("volume")
# timeOfTick = tick.get("time")
# print(volume, timeOfTick)

from threading import Thread

counter = 0
while counter != 5:
    print(counter)
    Thread(target=CA.repeatGetPriceThreadTest("ADA-USD")).start()
    Thread(target=CA.repeatGetPriceThreadTest("ACH-USD")).start()
    Thread(target=CA.repeatGetPriceThreadTest("IOTX-USD")).start()
    Thread(target=CA.repeatGetPriceThreadTest("ETH-USD")).start()
    Thread(target=CA.repeatGetPriceThreadTest("ALGO-USD")).start()
    counter += 1
    CA.time.sleep(5)
