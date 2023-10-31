"""more scores. Ask the user for a number of scores and generates """

from random import randint


def main():
    """ask about the number of scores and generates random scores with a grade"""
    number_of_scores = int(input("How many scores you want?:"))

    for i in range(number_of_scores):
        random_score = randint(0, 100)
        random_grade = determine_grade(random_score)
        print(f"{random_score} is {random_grade}")


def determine_grade(score):
    """determine the grade of the given score"""
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"

    return grade


main()
