import json

# Dictionary to store users and their data
user_database = {}


# load users data from file
def load_users():
    try:
        with open("user_data.json", "r") as file:
            data = file.read().strip()
            if not data:
                return {}
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Database file not found, Creating a new one ... ")
        with open("user_data.json", "w") as file:
            json.dump({}, file)
            return {}


# Save user data to a file
def save_users():
    global user_database
    with open("user_data.json", "w") as file:
        json.dump(user_database, file)

# Initialize user_database
user_database = load_users()

# Registration of new users
def register_user():
    print("REGISTER")
    # prompt username
    username = input("Please enter the user name:").strip()
    # verify if user exists
    if username in user_database:
        print("Username exists! Try again")
        return
    # prompt password
    password = input("please enter your password: ").strip()
    # character length validation
    if len(password) < 6:
        print("Password can't be less than 6 characters")
        return
    # confirm pass
    confirm_password = input("Confirm your password: ").strip()
    if confirm_password != password:
        print("passwords do not match! Please try again")
        return
    # store the data
    user_database[username] = {"password": password}
    save_users()
    print("Registration Successful")


# main program loop
while True:
    print("TaskTide")
    action = input("choose an action (register, login or exit): ")
    if action == "register":
        register_user()
    # elif action == "login":
    #     # login_user()    #uncomment when defined the function
    elif action == "exit":
        print("Exiting the system... \n Bye")
        exit()
    else:
        print("Invalid action please choose...")
