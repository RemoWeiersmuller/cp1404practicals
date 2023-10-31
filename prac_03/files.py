"""Question for prac 3 for files.oy"""


def main():
    """get a name and write to a file"""
    name = input("Username: ")
    write_name(name)


def write_name(name):
    """write a given name in file"""
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()


main()

"""Read the name.txt file an print the content"""


def main():
    """print content of name.txt file"""
    in_file = open("name.txt", "r")
    print(f"Your name is {in_file.read()}")


main()

"""Question 3 """


def main():
    """sum of first 2 lines in file"""
    filename = "numbers.txt"
    in_file = open(filename, "r")
    total = 0
    for line in range(2):
        total += int(in_file.readline())
    print(total)
    in_file.close()


main()

"""Question 4"""


def main():
    """sum of all numbers in file"""
    filename = "numbers.txt"
    in_file = open(filename, "r")
    total = 0
    for line in in_file:
        total += int(line.strip())
    print(total)
    in_file.close()


main()
