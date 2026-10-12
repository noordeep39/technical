# Password Validator
# Write a Python program that validates a user's password.

# A password is considered valid if:
# It contains at least 8 characters
# It contains at least one uppercase letter
# It contains at least one lowercase letter
# It contains at least one digit

# The program should display whether the password is valid or invalid.


password = input("Enter password: ");

has_upper = False;
has_lower = False;
has_digit = False;

if password >= 8: #had atleast so it should be >=

    for char in password:

        if char.isupper():
            has_upper == True;

        elif char.islower():
            has_lower == True;

        elif char.isdigit():
            has_digit = True; # bug = should be true

    if has_upper and has_lower and has_digit: #bug = logical operators
        print("Valid Password");
    else:
        print("Invalid Password");

else:
    print("Invalid Password");