#Title: whatabook.py
#Author: Tara Botts
#Date: September 28, 2021
#Description: Assignment 12.2

#Import statements
import mysql.connector
from mysql.connector import errorcode

#Database config object
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

#Main Menu formatting
def show_menu():
    print("\nMAIN MENU")

    print("     1. View Books\n     2. View Store Locations\n     3. My Account\n     4. Exit Program")

    try:
        choice = int(input('\nPlease Enter Selection: '))

        return choice
    except ValueError:
        print("\nINVALID INPUT ERROR: PROGRAM TERMINATED\n")

        sys.exit(0)

#List of books formatting
def show_books(_cursor):
    
    #Inner join query for books 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    #Get results from the books cursor 
    books = _cursor.fetchall()

    print("\nLIST OF BOOKS")
    
    #Iterate over book data and display data 
    for book in books:
        print("\n     Book ID Number: {}\n     Book Name: {}\n     Author: {}\n     Details: {}\n".format(book[0], book[1], book[2], book[3]))

#List of locations formatting
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale, hours from store")

    locations = _cursor.fetchall()

    print("\nSTORE LOCATIONS")

    for location in locations:
        print("\n     Locale: {}\n     Hours: {}\n".format(location[1], location[2]))

#Validation of user ID
def validate_user():
    """ validate the users ID """

    try:
        user_id = int(input('\nEnter User ID Number: '))

        if user_id < 0 or user_id > 3:
            print("\nINVALID USER ID NUMBER ERROR: PROGRAM TERMINATED\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\nINVALID USER ID NUMBER ERROR: PROGRAM TERMINATED\n")

        sys.exit(0)

#My user account menu formatting
def show_account_menu():
    """ display the users account menu """

    try:
        print("\nMY ACCOUNT MENU")
        print("\n     1. Wishlist\n     2. Add Book\n     3. Main Menu")
        account_option = int(input('\nPlease Enter Selection: '))

        return account_option
    except ValueError:
        print("\nINVALID OPTION NUMBER ERROR: PROGRAM TERMINATED\n")

        sys.exit(0)

#Setting up inner joins for wishlist
def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\nMY WISHLIST")

    for book in wishlist:
        print("Book Name: {}\nAuthor: {}\n".format(book[4], book[5]))

#Formatting add books
def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlist """

    query = ("SELECT book_id, book_name, author, details " +
            "FROM book " +
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\nAVAILABLE BOOKS")

    for book in books_to_add:
        print("\n     Book ID: {}\n     Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    #Connecting to WhatABook database
    db = mysql.connector.connect(**config) 

    #Define cursor for MySQL queries
    cursor = db.cursor() 

    #Display Welcome
    print("\nWelcome to WhatABook! ")

    #Display Main Menu
    user_selection = show_menu() 

    #While user selection is not 4
    while user_selection != 4:

        #If user selects 1, call show_books method and display list of books
        if user_selection == 1:
            show_books(cursor)

        #If user selects 2, call show_locations method and display store locations and hours
        if user_selection == 2:
            show_locations(cursor)

        #If user selects 3, call validate_user method to validate user_id entered then call the show_account_menu() to display my user account menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            #While user selection is not 3
            while account_option != 3:

                #If user selects 1, call the show_wishlist() method to show the current books 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                #If user selects 2, call the show_books_to_add function
                if account_option == 2:

                    #Show books not currently in the user's wishlist
                    show_books_to_add(cursor, my_user_id)

                    #User input book id number
                    book_id = int(input("\nPlease enter the Book ID number you want to add: "))
                    
                    #Formatting the add of selected book to the user's wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    #commit changes to database
                    db.commit()

                    #Display book has been added message
                    print("\nBook ID: {} has been added to your wishlist!".format(book_id))

                #If user selects option less than 0 or greater than 3, display invalid option message 
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please retry...")

                #Return to my user account menu 
                account_option = show_account_menu()
        
        #If user selects option less than 0 or greater than 4, display an invalid option message
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please retry...")
            
        #Return to main menu
        user_selection = show_menu()

    #Display thank you message and end program
    print("\n\nTHANK YOU FOR USING WHATABOOK! \n\nPROGRAM TERMINATED")

except mysql.connector.Error as err:
#Display if error when connecting to MySQL

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    #Closes MySQL connection
    db.close()