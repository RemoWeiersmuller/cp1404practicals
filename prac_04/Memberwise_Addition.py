numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6, 4]


def main():
    combined_numbers = zip(numbers_1, numbers_2)

    total_numbers = [x + y for x, y in combined_numbers]

    print(total_numbers)


# TODO how to handle the case if one list is shorter?
# "add_memberwise([1, 2, 3], [1, 2, 3, 4]) would return [2, 4, 6, 4]"

main()
