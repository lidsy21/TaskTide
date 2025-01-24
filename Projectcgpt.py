# Dictionary
user_names_database = {}
password_database = {}

# Prompt user to enter their username and password
user_name = input("Please enter your username: ").strip().title()
password = input("Please enter your password: ").strip()


# Function to validate the username and password
def validate_credentials(username, password):
    return username in user_names_database and password in password_database


# Check if entered credentials are valid
if validate_credentials(user_name, password):
    print("Login Successful. You will be shortly redirected to your account page.")
else:
    print("Login failed. Please try again.")
    print("If you cannot remember, choose 'Forget Password' below.")

    # Allow the user to try again until they get it right
    while True:
        user_name = input("Please enter your username: ").strip().title()
        password = input("Please enter your password: ").strip()

        if validate_credentials(user_name, password):
            print("Login Successful. You will be shortly redirected to your account page.")
            break

