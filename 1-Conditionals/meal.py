x = input("What time is it? ")
y = x.split(":")
z = int(y[0])
a = int(y[1])

if z == 7 and a <= 59:
    print("breakfast time")
if z == 8 and a == 0:
    print("breakfast time")

if z == 12 and a <= 59:
    print("lunch time")
if z == 1 and a <= 59:
    print("lunch time")

if z == 18 and a <= 59:
    print("dinner time")
if z == 19 and a == 0:
    print("dinner time")
