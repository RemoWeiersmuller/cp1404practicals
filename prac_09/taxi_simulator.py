"""
Estimate: 60 minutes
Actual:   90minutes
Taxi Simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run a taxi simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    bill_to_date = 0

    print(MENU)
    menu_choice = input('>>>').upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            print('Taxi available:')
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")
            try:
                current_taxi = taxis[int(taxi_choice)]
            except IndexError:
                print('Invalid taxi choice')
            except ValueError:
                print('Choice has to be number')
        elif menu_choice == 'D':
            if current_taxi is None:
                print('You need to choose a taxi before you can drive')
            else:
                distance = get_valid_number_above_zero('Drive how far?')
                current_taxi.start_fare()
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${float(current_taxi.get_fare()):.2f}")
                bill_to_date += float(current_taxi.get_fare())
        else:
            print('Invalid option')
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        menu_choice = input('>>>').upper()
    print(f"Bill to date: ${bill_to_date:.2f}")
    print('Taxi are now:')
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all taxis with a number to choose."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_number_above_zero(prompt):
    """Get a valid number from the user above zero."""
    value = ''
    while value == '':
        try:
            value = float(input(prompt))
            if value <= 0:
                print('Number must be > 0')
                value = ''
        except ValueError:
            print('Invalid input; enter a valid number.')
            value = ''
    return value


if __name__ == '__main__':
    main()
    # run_test()
