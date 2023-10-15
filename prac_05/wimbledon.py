"""Read records and display all champions and their country."""
"""
Wimbledon
Estimate: 30 minutes
Actual:   45 minutes
"""


FILENAME = 'wimbledon.csv'
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read records and display all champions and their country."""
    records = read_records(FILENAME)
    display_champions(records)
    display_champions_country(records)


def display_champions_country(records):
    """Display the belonging countries of the champions."""
    countries = []
    for record in records:
        if not record[INDEX_COUNTRY] in countries:
            countries.append(record[INDEX_COUNTRY])
    print(f'\nThese {len(countries)} countries have won Wimbledon:')
    print((', '.join(sorted(countries))))


def display_champions(records):
    """Display the champions and the number of titles."""
    champion_to_count = {}
    for record in records:
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    print('Wimbledon Champions:')
    for champion, count in champion_to_count.items():
        print(champion, count)


def read_records(FILENAME):
    """Read the record and return it as a list of lists."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records


main()
