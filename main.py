''' Main file for Managing Library Users '''
import admin
import simple_user
#! /bin/python
# Dictionary
PASSWORD = {}
# Done SignUp
def save_signup(user_name,password):
    ''' Saving Username and Password '''
    if user_name and password:
        with open('file.txt','a',encoding='utf-8') as file:
            file.write(f'{user_name} {password} \n')
    else:
        print('Try Again')
# LogIn Module
def retrive():
    ''' Retriving Data from File and saave it in a dictionary '''
    with open('file.txt','r',encoding='utf-8') as f:
        for k in f:
            i = k.split(' ')
            PASSWORD[i[0]] = i[1]

def login(_username,_password):
    ''' Check UserName and Password '''
    if PASSWORD[_username] == _password:
        return True
    else:
        return False

# Library Menu Main Function for Control
def library_menu():
    ''' Library Management Menu '''
    while True:
        print('Welcome to the Library What you want to do')
        choose = int(input('1) SignUp 2) LogIn 3) Quit :'))
        if choose == 1:
            # SignUp logic
            user_name = input('Enter User Name: ')
            password = input('Enter password: ')
            save_signup(user_name,password)
        elif choose == 2:
            # LogIn logic
            login_username = str(input('Enter UserName: '))
            login_password = str(input('Enter password: '))
            if login_username == 'Admin' and login_password == 'Admin':
                admin.admin_user()
            else:
                retrive()
                status = login(login_username,login_password)
                if status:
                    simple_user.normal_user()
                else:
                    print('Invalid UserName or Password')
        elif choose == 3:
            # Quit the Process
            break
library_menu()
# Library Menu is Done
