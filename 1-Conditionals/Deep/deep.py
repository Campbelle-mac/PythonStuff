x = input("What is the answer to the Great life, the Universe, and Everything? ")

match x:
    case (
        "Forty two"
        | "forty two"
        | "Forty Two"
        | "forty-two"
        | "Forty-two"
        | "Forty-Two"
        | "42"
    ):
        print("Yes")
    case _:
        print("No")
