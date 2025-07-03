
firstpassword = input("Enter a new password: ")
secondpassword = input("Re-enter the password to confirm: ")

if firstpassword == secondpassword:
    print("Password Set Successfully!")
else:
    print("Error: Passwords do not match. Please try again.")
