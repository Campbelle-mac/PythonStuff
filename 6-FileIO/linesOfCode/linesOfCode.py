import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few arguments!")
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Wrong file type!")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            count = 0
            for lines in file:
                stripped = lines.lstrip()
                if stripped == "" or stripped == "\n":
                    continue
                if stripped.startswith("#"):
                    continue
                count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist!")


if __name__ == "__main__":
    main()
