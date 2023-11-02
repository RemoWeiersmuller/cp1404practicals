"""
languages
Estimate: 90 minutes
Actual:   45 + XX minutes

"""

import datetime

from prac_07.project import Project
from operator import attrgetter

FILENAME = "projects.txt"
FILENAME_OUTPUTFILE = "projects_test.txt"
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n"
        "(A)dd new project\n(U)pdate project\n(Q)uit")


def main():
    print(MENU)
    menu_choice = input('>>>').upper()
    while menu_choice != 'Q':
        if menu_choice == 'L':
            projects = read_file()
        elif menu_choice == 'S':
            save_projects(projects)
            print(f"project records have been saved to {FILENAME_OUTPUTFILE}")
        elif menu_choice == 'D':
            complete_projects, incomplete_projects = create_sorted_lists(projects)
            display_projects(complete_projects, incomplete_projects)
        elif menu_choice == 'F':
            print("filter")
        elif menu_choice == 'A':
            print("Let's add a new project")
            add_project(projects)
            print(projects)
        elif menu_choice == 'U':
            for i, project in enumerate(projects):
                print(i, project)
            new_percentage, new_priority, project_choice = get_new_object_values(projects)
            update_object(new_percentage, new_priority, project_choice, projects)



        else:
            print('Invalid menu menu_choice')
        print(MENU)
        menu_choice = input('>>>').upper()


def update_object(new_percentage, new_priority, project_choice, projects):
    if new_percentage != '':
        projects[project_choice].completion_percentage = new_percentage
    if new_priority != '':
        projects[project_choice].priority = new_priority


def get_new_object_values(projects):
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    return new_percentage, new_priority, project_choice


def display_projects(complete_projects, incomplete_projects):
    print("Incomplete projects: ")
    for line in incomplete_projects:
        print(line)
    print("Complete projects: ")
    for line in complete_projects:
        print(line)


def create_sorted_lists(projects):
    incomplete_projects = [project for project in projects if project.is_incomplete()]
    incomplete_projects.sort(key=attrgetter("priority"))
    complete_projects = [project for project in projects if not project.is_incomplete()]
    complete_projects.sort(key=attrgetter("priority"))
    return complete_projects, incomplete_projects


def add_project(projects):
    name = input("Name: ")
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $ "))
    percent_complete = int(input("Percent complete: "))
    projects.append(Project(name, date, priority, cost, percent_complete))


def save_projects(projects):
    with open(FILENAME_OUTPUTFILE, "w", encoding="utf-8-sig") as out_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(project.start_date)
            # date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
            # project_date = date.strftime("%d/%m/%Y"))
            print(f"{project.name} {project.start_date} {project.priority} "
                  f"{project.cost_estimate} {project.completion_percentage}", file=out_file)


def read_file():
    """Language file reader version using the csv module."""
    in_file = open(FILENAME, 'r', encoding="utf-8-sig")
    in_file.readline()  # skip the first line
    projects = []
    for line in in_file:
        name = line[:(line.find('/') - 2)].strip()
        start_date = line[(line.find('/') - 2):(line.find('/') + 8)].strip()
        parts = line[(line.find('/') + 8):].strip().split('\t')
        priority = parts[0]
        cost = parts[1]
        completion = parts[2]

        projects.append(Project(name, start_date, priority, cost, completion))
    in_file.close()
    print(projects)
    return projects


main()
