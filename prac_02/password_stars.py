"""Check the password"""


def main():
    """get valid password and display stars in the pw length"""
    minimum_length = 0

    password = get_password(minimum_length)

    print_stars(password)


def print_stars(password):
    """display stars in the length of the password given"""
    print('*' * len(password))


def get_password(minimum_length):
    """get a valid password"""
    password = input("your password:")
    while int(len(password)) <= minimum_length:
        print("invalid password")
        password = input("your password:")
    return password


main()
