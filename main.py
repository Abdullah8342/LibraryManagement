'''#! /bin/python'''
from admin import admin_user
from simpleUser import normalUser
import os
name = []
usernames = []
gmail = []
passwords = []

def save_file(fileName,mod,data_list):
    with open(fileName,mod,encoding='utf-8') as f:
        for item in data_list:
            f.write(item + '\n')

# check if the exist or not
def checkFile():
    path = '.username.txt' 
    file_present = os.path.exists(path)
    if file_present != True:
        try:
            save_file('name.txt','a',name)
            save_file('username.txt','a',usernames)
            save_file('gmail.txt','a',gmail)
            save_file('password.txt','a',passwords)
        except ImportError:
            print('Error occured')
    else:
        pass
checkFile()
# check if username and password are in the files or not 
def check(content,file,mod):
    with open(file,mod ,encoding='utf-8') as f:
        content = f.readlines()
    for x in content:
        x = x.strip()
        if name == x:
            return True
            break
        else:
            continue
def register():
    name.append(input("Enter your name: "))
    usernames.append(input("Choose your Username: "))
    gmail.append(input("Enter your Email: "))
    passwords.append(input("Enter your p@ssw0rd: "))
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    r_username = check(username,'username.txt','r')
    r_password = check(password,'password.txt','r')
    if r_username == 1 and r_password == 1:
        print('Welcome')
        normalUser()
    else:
        print('Invalid user')
def admin():
    print('UserName: Admin')
    admin_password = input('Enter Password: ')
    if admin_password == 'password':
        print("Welcome as Admin user")
        admin_user()
    else:
        print("Wrong password")
count = 0
while True:
    acount_ans = input("choose:  a)Sign Up     b)login     c)quit ")
    if acount_ans == 'a':
        count +=1
        register()
    elif acount_ans == 'b':
        user_login = str(input('choose: a)Admin user    b)Simple user: '))
        if user_login.lower() == 'a':
            admin()
        elif user_login.lower() == 'b':
            login()
    elif acount_ans == 'c':
        break
try:
    save_file('name.txt','a',name)
    save_file('username.txt','a',usernames)
    save_file('gmail.txt','a',gmail)
    save_file('password.txt','a',passwords)
except ImportError:
    print('Error occured')