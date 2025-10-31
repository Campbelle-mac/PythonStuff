amount = int(input("Price of Coke "))
coins = []
change = 0
x = 0
correct = False
customerCoin = input(Insert Coin: )

setCoin = input("Coins for machine: ")

while setCoin != "end":
    coins.append(setCoin)
    setCoin = input("Coins for machine: ")

while correct == False and x < len(coins):
    value = coins[x]
    if value == customerCoin:
        