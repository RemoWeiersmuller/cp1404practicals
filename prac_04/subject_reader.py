"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
subjects = []


def main():
    """Get data from txt file and display it."""
    data = get_data()
    print(data)
    display_subject_details(data)


def display_subject_details(data):
    """Display details about subject."""
    for details in data:
        print(f"{details[0]} is taught by {details[1]} and has {details[2]} students.")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subjects.append(parts)
        print("----------")
    input_file.close()
    return subjects


main()
