from db.connections import connections
from db.newDB import newDB

# set connection
conn, db = connections()

# Create new table
table_name = {

    #   name :          query

    'Book':   """   bookID INT PRIMARY KEY AUTO_INCREMENT,
                    bookNum VARCHAR(30) NOT NULL UNIQUE,
                    bookType VARCHAR(255),
                    bookTitle VARCHAR(255) NOT NULL,
                    bookPublisher VARCHAR(255),
                    bookYear YEAR,
                    bookAuthor VARCHAR(255),
                    bookPrice DECIMAL(10, 2),
                    bookAmount INT NOT NULL,
                    bookStock INT NOT NULL """,

    'User':  """    userID INT PRIMARY KEY AUTO_INCREMENT,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    membership VARCHAR(255) NOT NULL,
                    name VARCHAR(255)""",

    # Parent table
    'Record': """   recordID INT PRIMARY KEY AUTO_INCREMENT,
                    bookID INT NOT NULL,
                    borrowDate DATETIME NOT NULL,
                    returnDate DATETIME DEFAULT NULL,
                    userID INT NOT NULL,
                    FOREIGN KEY (bookID) REFERENCES Book(bookID),
                    FOREIGN KEY (userID) REFERENCES User(userID)"""

}

DB_init = newDB(conn=conn)
for key, value in table_name.items():
    DB_init.create_new_table(key, value.strip())
