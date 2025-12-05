def main():
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(plate):
    def correct_lenght(plate):
        if len(plate) >= 2 and len(plate) <= 6:
            return True
        else:
            print("Incorrect length")
            return False

    def two_letters(plate):
        if plate[0].isalpha() and plate[1].isalpha():
            return True
        else:
            print("Doesn't start with two letters")
            return False

    def num_pos(plate):
        found_number = False
        for char in plate:
            if found_number:
                if char.isalpha():
                    print("Number in the middle")
                    return False
                else:
                    continue
            else:
                if char.isdigit():
                    if char == "0":
                        print("Is 0")
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
            print("Not a number or letter")
            return False

    def is_valide(plate):
        if correct_lenght(plate) is False:
            return False
        if two_letters(plate) is False:
            return False
        if num_pos(plate) is False:
            return False
        if all_allowed(plate) is False:
            return False
        return True

    if is_valide(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
