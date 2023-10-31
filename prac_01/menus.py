"""
Programm with a menu

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""


def main():
    name = input('tell me your name: ')
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input("choice: ").upper()

    while choice != 'Q':
        if choice == 'H':
            print('hello', name)
        elif choice == 'G':
            print('goodbye', name)
        else:
            print('value is invalid')

        print("(H)ello\n(G)oodbye\n(Q)uit")
        choice = input("choice: ").upper()

    print('finished programm')


main()
