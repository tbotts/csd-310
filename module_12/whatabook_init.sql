/*
    Title: whatabook.sql
    Author: Tara Botts
    Date: September 28, 2021
    Description: Module 12 WhatABook Assignment
*/

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

/*
    Create tables
*/
CREATE TABLE store (store_id INT NOT NULL AUTO_INCREMENT, locale VARCHAR(500) NOT NULL, hour VARCHAR(50) NOT NULL, PRIMARY KEY(store_id)
);

CREATE TABLE book (book_id INT NOT NULL AUTO_INCREMENT, book_name VARCHAR(200) NOT NULL, author VARCHAR(200) NOT NULL, details VARCHAR(500), PRIMARY KEY(book_id)
);

CREATE TABLE user (user_id INT NOT NULL AUTO_INCREMENT, first_name VARCHAR(75) NOT NULL, last_name VARCHAR(75) NOT NULL, PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (wishlist_id INT NOT NULL AUTO_INCREMENT, user_id INT NOT NULL, book_id INT NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale, hour)
    VALUES('123 Main St., Disney, FL 34647', '9:00AM to 9:00PM');

/*
    insert book records 
*/
INSERT INTO book(book_id, book_name, details, author)
    VALUES('1', 'Anna Karenina', 'Published 1878', 'Leo Tolstoy');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('2', 'Madame Bovary', 'Published 1856', 'Gustave Flaubert');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('3', 'War and Peace', 'Published 1869', 'Leo Tolstoy');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('4', 'The Great Gatsby', 'Published 1925', 'F. Scott Fitzgerald'); 

INSERT INTO book(book_id, book_name, details, author)
    VALUES('5', 'Lolita', 'Published 1955', 'Vladimir Nabokov');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('6', 'Middlemarch', 'Published 1871', 'George Eliot');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('7', 'The Adventures of Huckleberry Finn', 'Published 1884', 'Mark Twain');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('8', 'In Search of Lost Time', 'Published 1913', 'Marcel Proust');

INSERT INTO book(book_id, book_name, details, author)
    VALUES('9', 'Night', 'Published 1960', 'Elie Wiesel');

/*
    insert users
*/ 
INSERT INTO user(user_id, first_name, last_name) 
    VALUES('1', 'Bradley', 'Davis');

INSERT INTO user(first_name, last_name)
    VALUES('2', 'Alessa', 'Barton');

INSERT INTO user(first_name, last_name)
    VALUES('3', 'Chelsey', 'Cooper');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bradley'), 
        (SELECT book_id FROM book WHERE book_name = 'Lolita')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Alessa'),
        (SELECT book_id FROM book WHERE book_name = 'War and Peace')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chelsey'),
        (SELECT book_id FROM book WHERE book_name = 'Night')
    );
