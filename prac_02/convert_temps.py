"""create temps_input.txt with random temperature in fahrenheit and converts it to celsius in an onther file"""

from random import uniform
from temperatures import convert_fahrenheit_to_celsius
from temperatures import convert_celsius_to_fahrenheit


def main():
    generate_fahrenheit_file()

    get_values_from_file()




def get_values_from_file():
    file = open('temps_input.txt', 'r')
    for i in range(15):
        value = file.readline()



def generate_fahrenheit_file():
    """generates file with 15 random floats"""
    with open('temps_input.txt', 'w') as f:
        for i in range(15):
            temperature = uniform(-200, 200)
            f.write(f"{temperature}\n")


main()
