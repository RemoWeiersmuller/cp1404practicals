password = input("your password:")
minimum_length = 0

while int(len(password)) <= minimum_length:
    print("invalid password")
    password = input("your password:")

print('*' * len(password))

