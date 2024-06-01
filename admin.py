#! /bin/python
global present
with open('books.txt','a') as f:
    pass
with open('books.txt','r') as first_char:
    f_char = first_char.read(1)
    if not f_char:
        present = 1
    else:
        present = 0

# Show the list of books if books are present
def show_books(fileName):
    try:
        with open(fileName,'r') as f:
            books_list = f.readlines()
            count = 1
        for x in books_list:
            x = x.strip()
            print("{}--> {}".format(count,x))
            count += 1
    except:
        print('No Books Present')
# For adding new book into the books list
def add_books(new_book):
    try:
        with open('books.txt','a') as f:
            f.write(new_book + '\n')
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
            if present == 1:
                print('No Book present')
            else:
                show_books('books.txt')
        elif choise == 'a':
            new_book = input('Enter book name: ')
            new_book_status = add_books(new_book.title())
            print(new_book_status)
        elif choise == 'd':
            if present == 1:
                print('Nothing for delet')
            else:
                show_books('books.txt')
                index = int(input('Enter Index of book for deleting '))
                if index > 0 and present != 1:
                    delet_status = delet_book(index)
                    print(delet_status)
                else:
                    print('Wrong Index Please Check,Try again')
        elif choise == 'q':
            break

# admin_user()