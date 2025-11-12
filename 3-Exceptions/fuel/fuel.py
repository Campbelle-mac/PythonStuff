def getPercent(x, y):
    Percent = round(x / y * 100)
    if Percent <= 1:
        return "E"
    elif Percent >= 99:
        return "F"
    else:
        return f"{Percent}%"


while True:
    Fraction = input("Fuel (input as x/y) ")
    try:
        FractionLs = Fraction.split("/")
        x = int(FractionLs[0])
        y = int(FractionLs[1])
        if y == 0 or x > y:
            print("Invalid. Try again")
            continue
    except (ValueError, ZeroDivisionError):
        print("Error. Try again")
    Percent = getPercent(x, y)
    print(Percent)
    break
