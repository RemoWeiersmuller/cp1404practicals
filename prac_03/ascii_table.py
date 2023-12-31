"""Program to get ASCII code or vis versa."""

LOWER_NUMBER = 33
UPPER_NUMBER = 127


def main():
    """Program to get ASCII code or vis versa with a list."""
    character = input("enter a character: ")
    print(ord(character))

    number = round(float(input(f"enter a number between {LOWER_NUMBER} and {UPPER_NUMBER}: ")))
    while number < LOWER_NUMBER or number > UPPER_NUMBER:
        print("number is invalid")
        number = round(float(input(f"enter a number between {LOWER_NUMBER} and {UPPER_NUMBER}: ")))
    print(chr(number))

    for i in range(LOWER_NUMBER, UPPER_NUMBER):
        print("{:>3}".format(i), chr(i))


main()
