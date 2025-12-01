import csv
import os
import sys

def read_file(input_file):
    if not os.path.exists(input_file):
        sys.exit("File does not exist.")
    orders = []
    try:
        with open(input_file) as file:
                reader = csv.DictReader(file)
                for line in reader:
                    orders.append(line)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
    return orders

def get_stats(orders):
    num_orders = 0
    total_rev = 0
    drink_freq = {}

    for order in orders:
        num_orders += 1
        total_rev += price float(order.get('price'))
        drink = order.get("drink")
        if drink in drink_freq:
            Drink_freq[drink] += 1
        else:
            Drink_freq[drink] == 1
    most_popular = []
    max_value = max(drink_freq.values())	
    for k, v in drink_freq.items():
        if v == max_value:
            most_popular.append(k)
    stats_tuple = (num_orders, total_rev, most_popular)
    return stats_tuple

if len(sys.argv) != 2:
    sys.exit("not enough arguments")
input_file = sys.argv[1]
orders = read_file(input_file)
num_orders, total_rev, most_popular = get_stats(orders)
print(f"Total number of orders: {num_orders}")
print(f"Total revenue: {total_rev}")
print(f"Most populat: {most_popular}")
