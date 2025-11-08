"""
CP1404/CP5632 Practical - Project Management Program
Estimated time: 6 hours
Actual time: 7 hours
Start time: 04/11/2025 00:00:00
"""

import datetime
from project import Project


def main():
    """Main program to manage projects."""
    print("Welcome to Pythonic Project Management")

    # Load projects from default file at startup
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    menu_choice = ""
    while menu_choice != "q":
        display_menu()
        menu_choice = input(">>> ").lower()

        if menu_choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif menu_choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(projects, filename)
            print(f"Projects saved to {filename}")

        elif menu_choice == "d":
            display_projects(projects)

        elif menu_choice == "f":
            filter_projects_by_date(projects)

        elif menu_choice == "a":
            projects = add_new_project(projects)

        elif menu_choice == "u":
            projects = update_project(projects)

        elif menu_choice == "q":
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice.startswith('y'):
                save_projects(projects, "projects.txt")
                print("Projects saved.")
            print("Thank you for using custom-built project management software.")

        else:
            print("Invalid menu choice")


def display_menu():
    """Display the main menu."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Load projects from file and return list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as file:
            # Skip header line
            next(file)
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    name, start_date, priority, cost_estimate, completion = parts
                    project = Project(name, start_date, priority, cost_estimate, completion)
                    projects.append(project)
    except FileNotFoundError:
        print(f"Error: File {filename} not found. Starting with empty project list.")
    return projects


def save_projects(projects, filename):
    """Save list of Project objects to file."""
    with open(filename, 'w') as file:
        # Write header
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display projects grouped by completion status and sorted by priority."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    # Sort both groups by priority
    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [p for p in projects if p.start_date_after(filter_date)]

        # Sort by date
        filtered_projects.sort(key=lambda x: x.start_date)

        print(f"\nProjects starting after {date_string}:")
        for project in filtered_projects:
            print(f"  {project}")

    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    """Add a new project from user input."""
    print("Let's add a new project")

    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print(f"{name} added successfully.")

    return projects


def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    # Display numbered list of projects
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            print(project)

            # Get new completion percentage (allow empty to keep current)
            new_completion = input("New Percentage: ")
            if new_completion:
                project.completion_percentage = int(new_completion)

            # Get new priority (allow empty to keep current)
            new_priority = input("New Priority: ")
            if new_priority:
                project.priority = int(new_priority)

            print("Project updated successfully.")
        else:
            print("Invalid project choice.")

    except (ValueError, IndexError):
        print("Invalid input.")

    return projects


if __name__ == "__main__":
    main()