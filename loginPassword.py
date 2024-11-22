correct_login = "12345"
correct_password = "67890"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_login = input("Enter login: ")
    user_password = input("Enter password: ")

    if user_login == correct_login and user_password == correct_password:
        print("Successfully logged in to the website!")
        break
    else:
        print("Incorrect login or password. Please try again.")
        attempts += 1

if attempts == max_attempts:
    print("Maximum login attempts reached. Please try again later.")