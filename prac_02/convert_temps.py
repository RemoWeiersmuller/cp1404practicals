"""create temps_input.txt with random temperature in fahrenheit and converts it to celsius in an onther file"""

from random import uniform


def main():
    with open('temps_input.txt', 'w') as f:
        for i in range(15):
            f.write(str(uniform(-200, 200)))


main()
