"""
Estimate: 60 minutes
Actual:    minutes
Taxi Simulator
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run a taxi simulator."""
    # taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    print(MENU)
    menu_choice = input('>>>').upper()
    while menu_choice != 'Q':
        if menu_choice == 'C':
            print('Taxi available:')
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
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
                print('drive')
        else:
            print('Invalid menu menu_choice')
        if current_taxi is None:
            print(f"Bill to date: $0.00")
        else:
            print(f"Bill to date: ${current_taxi.get_fare()}")
        print(MENU)
        menu_choice = input('>>>').upper()
    print('get fare')


main()
