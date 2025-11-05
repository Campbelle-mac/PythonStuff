food = {
    "Apple": "130 Calories",
    "Banana": "89 Calories",
    "Strawberry": "45 Calories",
    "Mango": "60 Calories",
}


def main():
    item = input("Items: ")
    items = item.split()
    for key in items:
        key = key.title()
        if key in food:
            print(key, "is", food[key])
        else:
            print(key, "not found")


"""def main():                 - Original problem 
    items = input("Items: ")
    key = item.lower()
    if key in food:
        print(food[key])
    else:
        print("Not found")"""


main()
