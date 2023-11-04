"""
languages
Estimate: 90 minutes
Actual:   45 + 90 + 120 + 120 = 375 minutes


Load project data from a file with options to display, add, update, filter and save projects.
"""

import datetime
from operator import attrgetter
from project import Project


FILENAME = "projects.txt"
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project\n(U)pdate project\n(Q)uit")


def main():
    """Load project data from a file with
    options to display, add, update, filter and save projects."""
    projects = read_file()
    print(MENU)
    menu_choice = input('>>>').upper()
    while menu_choice != 'Q':
        if menu_choice == 'L':
            projects = read_file()
        elif menu_choice == 'S':
            outputfile_name = save_projects(projects)
            print(f"project records have been saved to {outputfile_name}")
        elif menu_choice == 'D':
            display_projects(projects)
        elif menu_choice == 'F':
            filtered_projects = filter_projects(projects)
            for project in filtered_projects:
                print(project)
        elif menu_choice == 'A':
            print("Let's add a new project")
            add_project(projects)
        elif menu_choice == 'U':
            for i, project in enumerate(projects):
                print(i, project)
            update_object(projects)
        else:
            print('Invalid menu menu_choice')
        print(MENU)
        menu_choice = input('>>>').upper()

    save_choice = input("you want to save (y/n): ").upper()
    if save_choice == 'Y':
        outputfile_name = save_projects(projects)
        print(f"project records have been saved to {outputfile_name}")
    print("Thank you for using custom-built project management software.")


def read_file():
    """Load the data from a given txt file."""
    with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip the first line
        projects = []
        for line in in_file:
            name = line[:(line.find('/') - 2)].strip()
            date_string = line[(line.find('/') - 2):(line.find('/') + 8)].strip()
            start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            parts = line[(line.find('/') + 8):].strip().split('\t')
            priority = int(parts[0])
            cost = float(parts[1])
            completion = int(parts[2])
            projects.append(Project(name, start_date, priority, cost, completion))
    return projects


def save_projects(projects):
    """Save the projects in a txt file."""
    outputfile_name = get_valid_input("Enter name of the outputfile: ")
    with open(outputfile_name, "w", encoding="utf-8-sig") as out_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name} {project.start_date.strftime('%d/%m/%Y')} {project.priority} "
                  f"{project.cost_estimate} {project.completion_percentage}", file=out_file)
    return outputfile_name


def display_projects(projects):
    """Display the projects sorted by priority in two separated list."""
    incomplete_projects = [project for project in projects if project.is_incomplete()]
    incomplete_projects.sort(key=attrgetter("priority"))
    complete_projects = [project for project in projects if not project.is_incomplete()]
    complete_projects.sort(key=attrgetter("priority"))
    print("Incomplete projects: ")
    for line in incomplete_projects:
        print(line)
    print("Complete projects: ")
    for line in complete_projects:
        print(line)


def filter_projects(projects):
    """Filter the list of project by a entered date."""
    filter_date = get_valid_date()
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    return filtered_projects


def get_valid_date():
    """Get a valid date from the user and store it as a datetime object."""
    is_finished = False
    date_string = input("Show projects that start after date (dd/mm/yy):")  # e.g., "30/9/2022"
    while not is_finished:
        try:
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_finished = True
        except ValueError:
            print("invalid date")
            date_string = input("Show projects that start after date (dd/mm/yy):")
    return filter_date


def update_object(projects):
    """Update the values of a project with the given user inputs."""
    # project_choice = int(input("Project choice: "))
    project_choice = get_valid_number_or_empty_string("Project choice: ",
                                                      int, (len(projects) - 1), True)
    print(projects[project_choice])
    new_percentage = get_valid_number_or_empty_string("New Percentage: ", float)
    new_priority = get_valid_number_or_empty_string("New Priority: ", int)
    if new_percentage != '':
        projects[project_choice].completion_percentage = new_percentage
    if new_priority != '':
        projects[project_choice].priority = new_priority


def get_valid_number_or_empty_string(prompt, datatype, max_value=100, is_empty_inadmissible=False):
    """Get a valid number or an empty string from the User and checks the datatype. """
    is_finished = False
    while not is_finished:
        try:
            number = input(prompt)
            if number != '' or is_empty_inadmissible:
                number = datatype(number)
                assert number >= 0
                assert number <= max_value
            is_finished = True
        except ValueError:
            print("Enter a valid number")
        except AssertionError:
            print(f"Number is not in the given range, has to be <= {max_value}")
    return number


def add_project(projects):
    """Add a new project to the list of projects."""
    name = get_valid_input("Name: ")
    new_project_date = get_valid_date()
    priority = get_valid_number_or_empty_string("Priority: ", int)
    cost = get_valid_number_or_empty_string("Cost estimate: $ ", float, float('inf'))
    percent_complete = get_valid_number_or_empty_string("Percent complete: ", int)
    projects.append(Project(name, new_project_date, priority, cost, percent_complete))


def get_valid_input(prompt):
    """Get a valid input from the user."""
    value = input(prompt)
    while value == '':
        print('Input can not be blank.')
        value = input(prompt)
    return value


main()
