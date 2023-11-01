"""
languages
Estimate: 90 minutes
Actual:   XX minutes

"""

import datetime

FILENAME = "projects.txt"
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project\n(U)pdate project\n(Q)uit")


def main():
    print(MENU)
    choice = input('>>>').upper()
    while choice != 'Q':
        if choice == 'L':
            read_file()
        elif choice == 'S':
            print("save")
        elif choice == 'D':
            print("display")
        elif choice == 'F':
            print("filter")
        elif choice == 'A':
            print("add")
        elif choice == 'U':
            print("update")
        else:
            print('Invalid menu choice')
        print(MENU)
        choice = input('>>>').upper()


def read_file():
    """Language file reader version using the csv module."""
    in_file = open(FILENAME, 'r', encoding="utf-8-sig")
    in_file.readline()  # skip the first line
    for line in in_file:
        project_name = line[:(line.find('/') - 2)].strip()
        project_start_date = line[(line.find('/') - 2):(line.find('/') + 8)].strip()
        parts = line[(line.find('/') + 8):].strip().split('\t')
        priority = parts[0]
        cost = parts[1]
        completion = parts[2]
        print(project_name)
        print(project_start_date)
        print(priority)
        print(cost)
        print(completion)
        # parts = line.strip().split(' ')
        # print(parts)
        # language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        # # Add the language we've just constructed to the list
        # languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

main()
