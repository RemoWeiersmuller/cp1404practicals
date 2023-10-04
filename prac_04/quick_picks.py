from random import randint

number_quick_picks = int(input("How many quick picks?: "))
NUMBER_OF_NUMBERS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

quick_picks = []
for i in range(number_quick_picks):
    for j in range(NUMBER_OF_NUMBERS):
        random_number = randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in quick_picks:  # Checking if number is already part of the list
            random_number = randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(random_number)
        quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))
    quick_picks = []
