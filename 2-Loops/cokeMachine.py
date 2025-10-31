def correctcoin(coin):
    correct = False
    match coin:
        case 25 | 10 | 5:
            correct = True
    return correct


amount = 50
change = 0
print("Amount Due:", amount)

while amount > 0:
    coin = int(input("Insert Coin: "))
    valid = correctcoin(coin)
    if valid:
        amount = amount - coin
    if amount < 0:
        change = abs(change)
    else:
        if amount > 0:
            print("Amount Due:", amount)
print("Change Owed:", change)
