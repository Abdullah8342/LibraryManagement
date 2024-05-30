#! /bin/python
# Show the list of books if books are present
global count
count = 1
def show_books():
    try:
        with open('books.txt','r') as f:
            books_list = f.readlines()
        for x in books_list:
            x = x.strip()
            print("{}--> {}".format(count,x))
            count += 1
    except:
        print('No Books Present')
# For adding new book into the books list
def add_books(new_book):
    try:
        with open('books.txt','r') as file:
            books_list = file.readlines()
        if new_book not in books_list:
            with open('books.txt','a') as f:
                f.write(new_book + '\n')
            count +=1
        else:
            pass
    except:
        return ('Error Occur While adding new book Try again please')
    else:
        return ('New book Added')
# Deleting book from the list 
def delet_book(index):
    try:
        with open('books.txt','r') as f:
            lines = f.readlines()
            ptr = 1
            with open('books.txt','w') as f:
                for line in lines:
                    if index != ptr:
                        f.write(line)
                    ptr +=1
            return ('Book is Deleted')
    except:
        return ("Oops! something error")

def admin_user():
    while True:
        print('What did you want to do')
        choise = input('s)Show Books a)Add books d)Delet books q)Quit ')
        if choise == 's':
            if count == 1:
                print('No Book present')
            else:
                show_books()
        elif choise == 'a':
            new_book = input('Enter book name: ')
#            new_book = new_book.title()
            new_book_status = add_books(new_book)
            print(new_book_status)
        elif choise == 'd':
            if count == 1:
                print('Nothing for delet')
            else:
                show_books()
                index = int(input('Enter Index of book for deleting '))
                if index > 0 and count != 1:
                    delet_status = delet_book(index)
                    print(delet_status)
                else:
                    print('Wrong Index Please Check,Try again')
        elif choise == 'q':
            break
with open('books.txt','a') as f:
    pass
admin_user()
