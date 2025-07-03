password=input("Enter your password: ")
BAD_PASSWORDS=('password','letmein','sesame','hello','justinbieber')
if password not in BAD_PASSWORDS:
    print("Password Set")
else:
    print("Error ")



