"""
emails.py
Estimated time: [Please fill in your estimated time]
Actual time: [Please fill in your actual time]
"""

def extract_name(email):
    """Extract the name from the email by splitting the email prefix and formatting it"""
    prefix = email.split('@')[0]
    names = prefix.split('.')
    formatted_name = ' '.join(name.title() for name in names)
    return formatted_name

email_to_name = {}

email = input("Email: ")
while email != "":
    suggested_name = extract_name(email)
    confirm = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()
    if confirm == '' or confirm == 'y':
        name = suggested_name
    else:
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")