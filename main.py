#! /bin/python
name = []
usernames = []
gmail = []
passwords = []

def register():
    name.append(input("Enter your name: "))
    usernames.append(input("Choose your Username: "))
    gmail.append(input("Enter your Email: "))
    passwords.append(input("Enter your p@ssw0rd: "))
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in usernames and password in passwords:
        print("Welcome")
    else:
        print("incorrect username or password")
while True:
    acount_ans = input("choose:  a)Sign Up     b)login and shop     c)quit ")
    if acount_ans == 'a':
        register()
    elif acount_ans == 'b':
        login()
    elif acount_ans == 'c':
        break