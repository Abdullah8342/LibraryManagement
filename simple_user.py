''' Simple User can only Add,Remove Books from My Learning '''
#! /bin/python
import admin

def book(ind):
    ''' Returning the Book title From File Using Index '''
    with open('books.txt','r',encoding='utf-8') as f:
        content = f.readlines()
        pointer = 1
        for x in content:
            if pointer == ind:
                return x
            else:
                pass
            pointer +=1

def new_book(book_name):
    ''' Adding Book to The My Learning '''
    try:
        with open('mylearning.txt','a',encoding='utf-8') as f:
            f.write(book_name)
    except RuntimeError:
        print('Error While adding book to my learning')

def remove_book(ind):
    ''' Removing Book from My Learning '''
    try:
        with open('mylearning.txt','r',encoding='utf-8') as f:
            full_content = f.readlines()
            ptr = 1
            with open('mylearning.txt','w',encoding='utf-8') as file:
                for x in full_content:
                    if ptr != ind:
                        file.write(x)
                    else:
                        pass
                    ptr +=1
    except RuntimeError:
        print('Error Occur while Removing Book from My Learning')

def normal_user():
    ''' Normal User Module '''
    while True:
        print("What did you want to do")
        choise = input('s)Show Books from library a)Add book d)Remove book m)My_Learning q)Quit ')
        if choise == 's':
            admin.show_books('books.txt')
        elif choise == 'a':
            admin.show_books('books.txt')
            add_index = int(input('Enter the index of the book: '))
            book_name = book(add_index)
            new_book(book_name)
        elif choise == 'd':
            admin.show_books('mylearning.txt')
            remove_index = int(input('Enter the index of the book: '))
            remove_book(remove_index)
        elif choise == 'm':
            print('My Learning Status')
            admin.show_books('mylearning.txt')
        elif choise == 'q':
            break
# normalUser()
