import re

password = input("Enter a password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check uppercase letters
if re.search("[A-Z]", password):
    score += 1

# Check numbers
if re.search("[0-9]", password):
    score += 1

# Check special characters
if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1


# Determine strength
if score == 4:
    print("Password Strength: Strong")
elif score == 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
