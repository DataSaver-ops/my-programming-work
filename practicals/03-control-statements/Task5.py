BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter your new password (8-12 characters): ")
    password2 = input("Confirm your new password: ")
    if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        print("Password Set")
        break
    else:
        print("Error: Passwords do not match, do not meet the criteria, or are too common! Please try again.")
