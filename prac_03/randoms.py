"""
What did you see on line 1?
9, 8, 13 -> a random integer between 5 and 20.

What was the smallest number you could have seen, what was the largest?
smallest 5, largest 20

What did you see on line 2?
3, 7, 9 -> random number between 3 and 10 in steps by 2.

What was the smallest number you could have seen, what was the largest?
smallest 3, largest 9

Could line 2 have produced a 4?
no because the step is 2

What did you see on line 3?
3.398643659615688, 2.969985776729841 -> random float between 3.5 and 5.5
What was the smallest number you could have seen, what was the largest?
2.500000000000000, 5.500000000000000
Write code, not a comment, to produce a random number between 1 and 100 inclusive.

"""

from random import randint
def main():
    print(randint(1,100))

main()