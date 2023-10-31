import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    records = read_csv()
    for parts in records:
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    in_file = open(FILENAME, 'r', newline='')
    reader = csv.reader(in_file)  # use default dialect, Excel
    lines = []
    for row in reader:
        lines.append(row)
    in_file.close()
    return lines


main()
