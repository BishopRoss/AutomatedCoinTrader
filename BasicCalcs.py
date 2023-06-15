# 1. Increase = New Number - Original Number
# 2. % Increase = Increase / Original Number * 100


# This function will take an initial buy price, a sell price, and let you know the percentage gain or loss.
def percentGain(new, old):
    inc = new - old
    percInc = round((inc / old) * 100, 2)
    print(percInc)


# This function will take the desired percentage gain and an initial buy price and tell you
# what price to sell the coin at.
def whatPriceToSell(percGain, old):
    perc = percGain / 100 * old
    sellPrice = round(perc + old, 2)
    print(sellPrice)


print("This is the percentage gain for the price it may go up to and the price it is at now:")
percentGain(1.9, 1.6531)
print("This is the price you need to sell it at to make your desired gain:")
whatPriceToSell(35, 24.25)
