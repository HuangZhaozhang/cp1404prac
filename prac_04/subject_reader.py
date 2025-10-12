"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    subject_details = load_subject_data(FILENAME)
    display_subject_reports(subject_details)

def load_subject_data(filename=FILENAME):
    """Read data from file and return as a list of lists."""
    subject_list = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_list.append(parts)
    input_file.close()
    return subject_list

def display_subject_reports(subject_list):
    """Display formatted reports for each subject."""
    for subject in subject_list:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")

main()
