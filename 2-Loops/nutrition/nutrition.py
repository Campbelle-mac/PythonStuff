food = {
    "apple": "Calories: 130",
    "banana": "Calories: 89",
    "strawberry": "Calories: 45",
    "mango": "Calories: 60",
}


def main():
    item = input("Item: ")
    key = item.lower()
    if key in food:
        print(food[key])
    else:
        print("Not found")


main()
