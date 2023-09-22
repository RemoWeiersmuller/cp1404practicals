"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint


def main():
    """"get a score give back a grade"""
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)

    # random score
    random_score = randint(0, 100)
    random_grade = determine_grade(random_score)
    print(random_grade)


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


print(__name__)
if __name__ == "__main__":
    main()
