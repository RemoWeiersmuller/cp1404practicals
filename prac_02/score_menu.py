"""Score menu for practical 2"""

from score import determine_grade


def main():
    score = None
    print("(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit")
    choice = input("choice: ").upper()

    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            if score is not None:
                grade = determine_grade(score)
                print(grade)
            else:
                score = get_valid_score()
                grade = determine_grade(score)
                print(grade)
        elif choice == 'S':
            if score is not None:
                print('*' * score)
            else:
                score = get_valid_score()
                print('*' * score)
        else:
            print('value is invalid')

        print("(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input("choice: ").upper()

    print('farewell')


def get_valid_score():
    """get a valid score from user"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Score: "))
    return score


main()
