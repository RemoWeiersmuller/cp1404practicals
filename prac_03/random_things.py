"""Write 3 different versions of code to generate a random Boolean (True or False)."""

import random


def main():
    random_boolean1 = random.choice([True, False])
    print(random_boolean1)
    random_boolean2 = bool(random.getrandbits(1))
    print(random_boolean2)
    random_boolean3 = bool(random.randint(0, 1))
    print(random_boolean3)


main()
