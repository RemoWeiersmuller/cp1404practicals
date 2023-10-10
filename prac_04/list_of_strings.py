"""Write a program that asks the user for an indefinite set of strings - until an empty string is entered - then prints all of the strings that were entered more than once.
E.g. if the user entered: "hello", "world is good", "hello", "john", "good world"... the program would print "Strings repeated: hello".
If no repeated strings are entered, the program should print "No repeated strings entered"."""


strings = []
double_strings = []

word = input('enter a word: ')

while word != '':
    if word in strings:
        double_strings.append(word)
    strings.append(word)
    word = input('enter a word: ')

if len(double_strings) == 0:
    print('No repeated strings entered')

else:
    # Use set() to get unique duplicated words
    unique_duplicates = list(set(double_strings))
    for i in unique_duplicates:
        print(f"Strings repeated:", i)

