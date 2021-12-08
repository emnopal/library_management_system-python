from db.connections import connections
from db.newDB import newDB

# set connection
conn, db = connections()

# Create new table
table_name = {

    #   name :          query

    'book':   """   bookID INT PRIMARY KEY AUTO_INCREMENT,
                    bookNum VARCHAR(30) NOT NULL UNIQUE,
                    bookType VARCHAR(255),
                    bookTitle VARCHAR(255) NOT NULL,
                    bookPublisher VARCHAR(255),
                    bookYear YEAR,
                    bookAuthor VARCHAR(255),
                    bookPrice DECIMAL(10, 2),
                    bookAmount INT NOT NULL,
                    bookStock INT NOT NULL """,

    'card':   """   cardID INT PRIMARY KEY AUTO_INCREMENT,
                    cardNum VARCHAR(30) NOT NULL UNIQUE,
                    cardName VARCHAR(255) NOT NULL,
                    cardUnit VARCHAR(255),
                    cardType char(1) NOT NULL""",

    'admin':  """   userID INT PRIMARY KEY AUTO_INCREMENT,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    fullName VARCHAR(255),
                    phone VARCHAR(255),
                    email VARCHAR(255)""",

    # Parent table
    'record': """   recordID INT PRIMARY KEY AUTO_INCREMENT,
                    bookID INT NOT NULL,
                    cardID INT NOT NULL,
                    borrowDate DATETIME NOT NULL,
                    returnDate DATETIME,
                    userID INT NOT NULL,
                    FOREIGN KEY (bookID) REFERENCES Book(bookID),
                    FOREIGN KEY (cardID) REFERENCES Card(cardID),
                    FOREIGN KEY (userID) REFERENCES Admin(userID)"""

}

DB_init = newDB(conn=conn)
for key, value in table_name.items():
    DB_init.create_new_table(key, value.strip())
