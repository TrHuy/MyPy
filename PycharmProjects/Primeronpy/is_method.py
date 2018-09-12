# check input
print("Enter your name: ")
name = input()
while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("Please inter numbers for your age!")
while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("passwords can only have letters and numbers")