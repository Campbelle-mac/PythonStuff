words = input("Input: ")
newWords = ""
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

for char in words:
    if char in vowels:
        continue
    else:
        newWords = newWords + char

print("Output:", newWords)
