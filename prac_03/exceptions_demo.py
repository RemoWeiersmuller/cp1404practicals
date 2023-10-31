"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def main():

    try:
        numerator = int(input("Enter the numerator: "))
        get_valid_denominator()
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")

def get_valid_denominator():
    global denominator
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))


main()

"""
Questions
When will a ValueError occur?
if a string or a float

When will a ZeroDivisionError occur?
if 0 is given as the denominator

Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes 
"""