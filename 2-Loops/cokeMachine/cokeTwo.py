amount = int(input("Price of Coke: "))
coins = []
change = 0
x = 0
correct = False

setCoin = input("Coins for machine: ")

while setCoin != "end":
    coins.append(setCoin)
    setCoin = input("Coins for machine: ")

print("Buy a Coke")
print("Price:", amount)
customerCoin = input("Insert Coin: ")

while correct == False and amount > 0:
    value = coins[x]
    if value == customerCoin and amount > 0:
        correct = True
        customerCoinb = int(customerCoin)
        amount = amount - customerCoinb
        print("Price remaining:", amount)
        correct = False
    elif x < len(coins):
        print("Invalid coin, machine only accepts", coins, "coins.")
    if value == customerCoin and amount < 0:
        correct = True
        customerCoinb = int(customerCoin)
        amount = amount - customerCoinb
        amountb = str(amount)
        change = amountb[-1]
        print("Thank you, dispensing drink.")
        print("Change:", change)
        break
    x = x + 1
    customerCoin = input("Insert Coin: ")
