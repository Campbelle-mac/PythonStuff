def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove first value ($), convert d to float.
    converted = float(d[1:])
    return converted


def percent_to_float(p):
    # Remove last value (%), convert p to float and divide by 100.
    converted = float(p[:-1]) / 100
    return converted


main()
