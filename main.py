#! /bin/python
name = []
usernames = []
gmail = []
passwords = []

def save_file(fileName,mod,data_list):
    with open(fileName,mod) as f:
        for item in data_list:
            f.write(item + '\n')

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
def admin():
    print('UserName: Admin')
    admin_password = input('Enter Password: ')
    if admin_password == 'password':
        print("Welcome as Admin user")
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
except:
    print('Error occured')