def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    match greeting:
        case "Hey" | "How you doing?" | "How's it going?":
            return "$20"

        case "What's happening?" | "What's up?":
            return "$100"

        case _:
            return "$0"


if __name__ == "__main__":
    main()
