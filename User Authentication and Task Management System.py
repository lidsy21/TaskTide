# Dictionary to store users
user_database= {}
User_names_database = ['user_name']
password_database = ['0123456']

#Registration of new users
user_name = input("Please enter the user name:")
user_name.title()
password = input("please enter your password:")

if user_name == 'user_name' and password == '0123456':
    print('login Successful,you will be shortly redirected to your account page')
else:
    print('login fail,please try again\nif you cannot remember you should choose forget password below')
    while True:
        user_name = input("Please enter the user name:")
        user_name.title()
        password = input("please enter your password:")
        if euser_name == ' user_name' and password == '0123456':
            print('login Successful,you will be shortly redirected to your account page')