''' Admin User can add or delet Books from library '''
#! /bin/python

with open('books.txt','a', encoding='utf-8') as f:
    pass
with open('books.txt','r',encoding='utf-8') as first_char:
    f_char = first_char.read(1)
    if not f_char:
        PRESENT = 1
    else:
        PRESENT = 0

# Show the list of books if books are present
def show_books(file_name):
    ''' For Showing Books From Library '''
    try:
        with open(file_name,'r',encoding='utf-8') as file:
            books_list = file.readlines()
            count = 1
        for x in books_list:
            x = x.strip()
            print(f"{count}--> {x}")
            count += 1
    except RuntimeError:
        print('No Books Present')
# For adding new book into the books list
def add_books(new_book):
    ''' For Adding New Book to the Library '''
    try:
        with open('books.txt','a',encoding='utf-8') as file:
            file.write(new_book + '\n')
    except RuntimeError:
        return 'Error Occur While adding new book Try again please'
    else:
        return 'New book Added'
# Deleting book from the list
def delet_book(index):
    ''' For Deleting Books from Library '''
    try:
        with open('books.txt','r',encoding='utf-8') as file:
            lines = file.readlines()
            ptr = 1
            with open('books.txt','w',encoding='utf-8') as file:
                for line in lines:
                    if index != ptr:
                        file.write(line)
                    ptr +=1
            return 'Book is Deleted'
    except RuntimeError:
        return "Oops! something error"

def admin_user():
    ''' Admin Main Module '''
    while True:
        print('What did you want to do')
        choise = input('s)Show Books a)Add books d)Delet books q)Quit ')
        if choise == 's':
            if PRESENT == 1:
                print('No Book present')
            else:
                show_books('books.txt')
        elif choise == 'a':
            new_book = input('Enter book name: ')
            new_book_status = add_books(new_book.title())
            print(new_book_status)
        elif choise == 'd':
            if PRESENT == 1:
                print('Nothing for delet')
            else:
                show_books('books.txt')
                index = int(input('Enter Index of book for deleting '))
                if index > 0 and PRESENT != 1:
                    delet_status = delet_book(index)
                    print(delet_status)
                else:
                    print('Wrong Index Please Check,Try again')
        elif choise == 'q':
            break

# admin_user()
