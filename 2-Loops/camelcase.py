camelCase = input("camelcase: ")
snake = ""

for char in camelCase:
    if char.islower() == True:
        snake = snake + char
    else:
        snake = snake + "_"
        low_char = char.lower()
        snake = snake + low_char
print("snake-case:", snake)
