import sqlite3

# connection
db = sqlite3.connect("books-collection.db")

# cursor to control database
cursor = db.cursor()

# Note -> in excel just like our it contain many spreadsheets
# in sql we have many tables

# creating table

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Cursor -> Pointer to control db
# execute -> this method tells cursor to execute the action
# actions are expressed by SQL commands
# Create table
#  Books name

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

# Storing data in bb table (books)

# Sql is very sensetive language , if you make any typos it will not work
# so, we use sqlAlchemy