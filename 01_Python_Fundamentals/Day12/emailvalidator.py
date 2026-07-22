import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

# email = input("Enter an email address to validate: ")
# if validate_email(email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")