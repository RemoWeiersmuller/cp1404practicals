"""
Wimbledon
Estimate: 30 minutes
Actual:    minutes
"""

FILENAME = 'wimbledon.csv'

with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    for line in in_file:
        print(in_file.readline())
