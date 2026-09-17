with open("secret.txt", "r", encoding="utf-8") as file:
    saved_password = file.read().strip()

user_input = input("Please enter your password: ")

if user_input == saved_password:
    print("Access granted! Welcome.")
else:
    print("Access denied! Incorrect password.")