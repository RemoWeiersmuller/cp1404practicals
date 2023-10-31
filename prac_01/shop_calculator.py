"""Shop calculator programm to calculate the total price for a number of items, each with different prices. Then the
program computes and displays the total price of those items. If the total price is over $100, then a 10% discount is
applied to that total before the amount is displayed on the screen.

Example
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92

"""
total_price = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input(f"Price of item {(i + 1)}:"))
    total_price += price_of_item

if total_price > 100:
    total_price = total_price * 0.9
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
