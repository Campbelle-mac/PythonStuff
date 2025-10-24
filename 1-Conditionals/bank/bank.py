x = input("Greeting: ")

match x:
    case "Hey" | "How you doing?" | "How's it going?":
        print("$20")
    case "What's happening?" | "What's up?":
        print("$100")
    case _:
        print("$0")
