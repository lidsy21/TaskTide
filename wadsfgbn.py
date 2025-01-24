User_names_database = ['user_name']
password_database = ['0123456']
"""prompt user to enter his/her username"""
entered_user_name = input("Please enter the user name:")
entered_user_name.title()
entered_password = input("please enter your password:")

"""Check if the entered user name/password existing in the user data base of the website"""
if entered_user_name == 'user_name' and entered_password == '0123456':
    print('login Successful,you will be shortly redirected to your account page')
else:
    print('login fail,please try again\nif you cannot remember you should choose forget password below')
    while True:
        entered_user_name = input("Please enter the user name:")
        entered_user_name.title()
        entered_password = input("please enter your password:")
        if entered_user_name == ' user_name' and entered_password == '0123456':
            print('login Successful,you will be shortly redirected to your account page')