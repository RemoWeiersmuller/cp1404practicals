"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    menu = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            temperature = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(temperature)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            temperature = float(input("fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(temperature)
            print(f"Result: {celsius:.2f} °C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(temperature):
    """" Convert given temperature to degrees celsius"""
    celsius = 5 / 9 * (temperature - 32)
    return celsius


def convert_celsius_to_fahrenheit(temperature):
    """" Convert given temperature to fahrenheit"""
    fahrenheit = temperature * 9.0 / 5 + 32
    return fahrenheit


if __name__ == "__main__":
    main()
