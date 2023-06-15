# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# bf2580af-879c-5f03-bbd9-96552cb8182a bank of america payment method ID
import time
from coinbase.wallet.client import Client
import EmailTesting as ET

coinbase_API_key = "enter your key here"
coinbase_API_secret = "enter your secret key here"
client = Client(coinbase_API_key, coinbase_API_secret)


# This function will get the price of a coin once and display it on the screen.
def getPrice(curr_pair, coin):
    price = client.get_buy_price(currency_pair=curr_pair)

    print("Current %s price in %s: %s at %s" % (curr_pair, curr_pair, price.amount, time.ctime()))
    if float(price.amount) <= 0.25:
        print("Sell this coin now")
        ET.sendEmailAlert(coin, price.amount)
getPrice("API3-USD", "API3")

# This function will provide the price for a coin every x seconds.
def repeatGetPrice(curr_pair):
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter != 129600:
        print(counter)
        price = client.get_buy_price(currency_pair=curr_pair)
        print("Current %s price in %s: %s at %s" % (curr_pair, curr_pair, price.amount, time.ctime()))
        if float(price.amount) >= 13.49:
            sell = client.sell("DDX",
                               amount="4,492.23089921",
                               currency="IOTX",
                               payment_method="8db18fca-541f-5149-8cb9-3ba9d2b9ab20")  # this payment method is for
            # the fiat account
            print(sell)
            print("You sold and made a gain!")
            break
        elif float(price.amount) >= 0.13:
            ET.sendEmailAlert(curr_pair, price.amount)
        counter += 1
        time.sleep(5)
    print("Stop Execution : ", end="")
    print(time.ctime())


# This function was intended to display the details of each crypto account associated
# with an account
def accountInfo(coin):  # This function will show crypto account details
    # This will get me my account ID and account information
    accounts = client.get_account(coin)
    print(accounts.balance.amount)
    print("This is how much your %s wallet is worth: %s at %s" % (coin, accounts.native_balance.amount, time.ctime()))


# This function operates as a buy monitor. It will watch the price of the coin,
# and if the coin drops to a specified point a buy will be executed for a chosen amount.
def buyMonitorProto(curr_pair, coin, amount, low_point):
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter != 129600:
        print(counter)
        price = client.get_buy_price(currency_pair=curr_pair)
        print("Current %s price in %s: %s at %s" % (curr_pair, curr_pair, price.amount, time.ctime()))
        if float(price.amount) <= low_point:
            buy = client.buy(coin,
                             total=amount,
                             currency="USD",
                             payment_method="8db18fca-541f-5149-8cb9-3ba9d2b9ab20")
            print(buy)
            break
        counter += 1
        time.sleep(5)
    print("Stop Execution : ", end="")
    print(time.ctime())


# This function will monitor the value of a specified crypto wallet.
# When the Wallet raises to a certain value, it will sell all of the coin in that wallet.
# If the wallet drops to a certain value, it will also sell all the coin at a specified loss.
def coinSellMonitor(coin, curr_pair, high_point):
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter != 129600:  # This is a day's worth of requests
        print(counter)
        price = client.get_buy_price(currency_pair=curr_pair)
        print("Current %s price in %s: %s at %s" % (curr_pair, curr_pair, price.amount, time.ctime()))
        if float(price.amount) >= high_point:  # This condition is a potential parameter
            accounts = client.get_account(coin)
            coinAmount = accounts.balance.amount
            sell = client.sell(coin,
                               amount=coinAmount,
                               currency="USD",
                               payment_method="8db18fca-541f-5149-8cb9-3ba9d2b9ab20")  # this payment method is for
            # the fiat account
            print(sell)
            print("You sold and made a gain!")
            break
        counter += 1
        time.sleep(7)
    print("Stop Execution : ", end="")
    print(time.ctime())


# This function will return the prices of a list of coins
def getPriceOfLOC():
    coins = ['ETH-USD', 'ICP-USD', 'CLV-USD',
             'ALGO-USD', 'ATOM-USD', 'GRT-USD',
             'BTC-USD', 'XTZ-USD', 'ACH-USD',
             'FET-USD', 'POLY-USD', 'CTSI-USD']
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter < 400:
        print(counter)
        for i in range(len(coins)):
            price = coins[i]
            getPrice(price)
        counter += 1
        time.sleep(2)
    print("Stop Execution : ", end="")
    print(time.ctime())


# This function will show the current prices of a couple of coins.
def getPriceOfLOC2():
    coins = ['IOTX-USD', 'ORN-USD']
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter != 3600:
        print(counter)
        for i in range(len(coins)):
            price = coins[i]
            getPrice(price)
        counter += 1
        time.sleep(2)
    print("Stop Execution : ", end="")
    print(time.ctime())


# This function is a basic operation where the coin and amount of coin to be bought
# is specified and a buy order is executed
def buyCoin(coin, amount):
    buy = client.buy(coin,
                     total=amount,
                     currency="USD",
                     payment_method="8db18fca-541f-5149-8cb9-3ba9d2b9ab20")
    print(buy)


# This function is a basic operation where a coin of choice is sold and deposited in the fiat account
def sellCoin():
    sell = client.sell("REQ",
                       total="4",
                       currency="USD",
                       payment_method="8db18fca-541f-5149-8cb9-3ba9d2b9ab20")  # this payment method if for the fiat account
    print(sell)


# This will return all the buys that have been executed on the account
def getBuys():
    txs = client.get_buys()
    print(txs)


# This function will return all the payment methods associated with the account
def paymentMethods():
    payment_methods = client.get_payment_methods()
    print("Here are your payment methods:")
    print(payment_methods)


# This was the test module that watched the value of the chosen crypto wallet
def coinMonitorTest(coin):
    accounts = client.get_account(coin)
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter != 43200:  # This is a day's worth of requests
        print(counter)
        accountInfo(coin)
        if float(accounts.native_balance.amount) >= 200.00:
            print("You sold at a 20% gain!")
            break
        elif float(accounts.native_balance.amount) <= 400.00:
            print("You sold at a 15% loss!")
            break
        counter += 1
        time.sleep(2)
    print("Stop Execution : ", end="")
    print(time.ctime())


# This was the original sell monitor. It sold based off of the amount of money held in a crypto wallet
def coinSellMonitor2(coin):
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter != 36000:
        accounts = client.get_account(coin)
        print(counter)
        print(
            "This is how much your %s wallet is worth: %s at %s" % (coin, accounts.native_balance.amount, time.ctime()))
        if float(accounts.native_balance.amount) >= 800.00:
            sell = client.sell("REQ",
                               amount="2,446.43469552",
                               currency="REQ",
                               payment_method="8db18fca-541f-5149-8cb9-3ba9d2b9ab20")  # this payment method is for
            # the fiat account
            print(sell)
            print("You sold and made a gain!")
            break
        counter += 1
        time.sleep(2)
    print("Stop Execution : ", end="")
    print(time.ctime())


def emailWatcher(curr_pair, price_point):
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter != 129600:
        print(counter)
        price = client.get_buy_price(currency_pair=curr_pair)
        if float(price.amount) <= float(price_point):
            ET.sendEmailAlert(curr_pair, price.amount)
            break
        counter += 1
        time.sleep(30)
    print("Stop Execution : ", end="")
    print(time.ctime())


def emailerForList():
    coins = ['ALGO-USD', 'ACH-USD', 'IOTX-USD', 'ETH-USD', 'ADA-USD']
    print("Start Execution : ", end="")
    print(time.ctime())
    counter = 0
    while counter < 400:
        print(counter)
        for i in range(len(coins)):
            price = client.get_buy_price(currency_pair=coins[i])
            print(price.amount)

        counter += 1
        time.sleep(2)
    print("Stop Execution : ", end="")
    print(time.ctime())


def repeatGetPriceThreadTest(curr_pair):
    # print("Time : ", end="")
    # print(time.ctime())
    price = client.get_buy_price(currency_pair=curr_pair)
    print("Current %s price in %s: %s at %s" % (curr_pair, curr_pair, price.amount, time.ctime()))
    # print("Stop Execution : ", end="")
    # print(time.ctime())
