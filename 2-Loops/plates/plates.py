plate = input("Plate: ")


def correct_lenght(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        return True
    else:
        return False


def two_letters(plate):
    if plate[0].isalpha() and plate[1].isalpha():
        return True
    else:
        return False


def num_pos(plate):
    found_number = False
    for char in plate:
        if found_number is False:
            if char.isalpha():
                return False
            else:
                continue
        else:
            if char.isdigit():
                if char == "0":
                    return False
                else:
                    found_number = True
            else:
                continue
        return True


def all_allowed(plate):
    if plate.isalnum():
        return True
    else:
        return False


def is_valid(plate):
    if correct_lenght(plate) is False:
        return False
    if two_letters(plate) is False:
        return False
    if num_pos(plate) is False:
        return False
    if all_allowed(plate) is False:
        return False
    return True


if is_valid(plate):
    print("Valid")
else:
    print("Invalid")
