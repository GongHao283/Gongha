# This program compares two strings and if the pair of the string is match then show greeting otherwise kick out
# Set password
password = "ChadISAwesome"
# Get input of password
inp_password = input("Please nter the password:")
# If the inputed password is same to the password then show greeting message
if inp_password == password:
    print("Hello, good to see you!")
# Otherwise, shows bye bye message
else:
    print("Sorry, your password is wrong,Bye bye!")