Menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
total = 0

while True:
    try:
        x = input("Item: ")
        food = x.title()
    except EOFError:
        print(f"Total: ${total}")
        break
    if food in Menu:
        itemPrice = Menu[food]
        total = total + itemPrice
        print(f"Total: ${total}")
