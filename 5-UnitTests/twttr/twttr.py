def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    new_word = ""
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for char in word:
        if char in vowels:
            continue
        else:
            new_word = new_word + char
    return f"Output: {new_word}"


if __name__ == "__main__":
    main()
