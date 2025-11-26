import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Not enough arguments")

input = sys.argv[1]
output = sys.argv[2]

try:
    with open(input, "r") as infile:
        reader = csv.DictReader(infile)

    with open(output, "w") as outfile:
        colnames = ["first", "last", "house"]
        writer = csv.DictWriter(outfile, fieldnames=colnames)
        writer.writeheader()

        for row in reader:
            last, first = row.split["name", ","]
            house = row["house"]
            write_dict = {"first": first, "last": last, "house": house}
            writer.writerow(write_dict)
except FileNotFoundError:
    sys.exit("File not found")
