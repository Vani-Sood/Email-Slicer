def email_slicer(email):
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    return f"Your username is {username} & domain is {domain}"
user_input = input("Enter Your Email: ")
print(email_slicer(user_input))