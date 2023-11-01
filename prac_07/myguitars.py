"""Read, display guitars from a csv and adds new guitars from user input and saves it back to the csv."""

import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read, display guitars from a csv and adds new guitars from user input and saves it back to the csv."""
    guitars = []
    records = read_csv()
    for record in records:
        guitar = Guitar(record[0], record[1], float(record[2]))
        guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    add_new_guitar(guitars)
    save_guitars(guitars)


def read_csv():
    """Language file reader version using the csv module."""
    in_file = open(FILENAME, 'r', newline='')
    reader = csv.reader(in_file)  # use default dialect, Excel
    lines = []
    for row in reader:
        lines.append(row)
    in_file.close()
    return lines


def add_new_guitar(guitars):
    """Add new guitars from user input to the list."""
    print("\nProvide details about your new guitar.")
    new_guitar_name = input("Name: ")
    while new_guitar_name != '':
        new_guitar_year = int(input("Year: "))
        new_guitar_price = float(input("Price: "))
        guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_price)
        guitars.append(guitar)
        print("New guitar added to list")
        new_guitar_name = input("Name: ")


def save_guitars(guitars):
    """Save all the guitars records to a CSV-file."""
    with open(FILENAME, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
