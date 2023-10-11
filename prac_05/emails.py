"""
Emails
Estimate: 25 minutes
Actual:   31 minutes
"""

name_to_email = {}

# email = input('enter your email: ')

email = 'remo.weiersmueller@gmail.com'

while email != '':
    part_before_at = email[:(email.find('@'))]
    name = (' '.join(part_before_at.split('.'))).title()

    is_correct = input(f"is your name {name}? (y/n)").lower()

    if not (is_correct == '' or is_correct == 'y'):
        print('wrong')
        name = input('enter your name: ').title()

    name_to_email[name] = email
    email = input('enter your email: ')


print('') # one space line between the list and the input.
for name, email in name_to_email.items():
    print(f"{name} ({email})")