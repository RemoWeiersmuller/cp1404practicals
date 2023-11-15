"""Silver servic taxi class test"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    my_silver_service_taxi = SilverServiceTaxi(name='Hummer', fuel=200, fanciness=4)
    print(my_silver_service_taxi)

    limo_silver_service_taxi = SilverServiceTaxi(name='Limo', fuel=200, fanciness=2)
    limo_silver_service_taxi.start_fare()
    limo_silver_service_taxi.drive(18)
    print(limo_silver_service_taxi.get_fare())


main()
