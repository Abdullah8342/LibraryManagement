#! /bin/python
import admin

def book(ind):
    with open('books.txt','r') as f:
        content = f.readlines()
        pointer = 1
        for x in content:
            if pointer == ind:
                return x
            else:
                pass
            pointer +=1

def newBook(bookName):
    try:
        with open('mylearning.txt','a') as f:
            f.write(bookName)
    except IndexError:
        print('Error While adding book to my learning')

def removeBook(ind):
    try:
        with open('mylearning.txt','r') as f:
            fullContent = f.readlines()
            ptr = 1
            for x in fullContent:
                with open('mylearning.txt','w') as file:
                    if ptr != ind:
                        file.write(x)
                    else:
                        pass
                    ptr +=1
    except ImportError:
        print('Error Occur while Removing Book from My Learning')

def normalUser():
    while True:
        print("What did you want to do")
        choise = input('s)Show Books from library a)Add book d)Remove book m)My_Learning q)Quit ')
        if choise == 's':
            admin.show_books('books.txt')
        elif choise == 'a':
            admin.show_books('books.txt')
            addIndex = int(input('Enter the index of the book: '))
            bookName = book(addIndex)
            newBook(bookName)
        elif choise == 'd':
            admin.show_books('mylearning.txt')
            removeIndex = int(input('Enter the index of the book: '))
            removeBook(removeIndex)
        elif choise == 'm':
            print('My Learning Status')
            admin.show_books('mylearning.txt')
        elif choise == 'q':
            break
normalUser()