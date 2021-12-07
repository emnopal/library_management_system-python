from db.connections import connections
from src.BookOperations import BookOperations

# set connection
conn, db = connections()

# insert into book
data_to_insert = {
    1:  {"bookID":1,  "bookNum": "book1",  "bookType": "Science",  "bookTitle": "Introduction to Quantum Mechanics",     "bookPublisher": "pub0", "bookYear": "1996", "bookAuthor": "au0", "bookPrice": 1000000, "bookAmount": 10},
    2:  {"bookID":2,  "bookNum": "book2",  "bookType": "Science",  "bookTitle": "Introduction to Electrodynamics",       "bookPublisher": "pub0", "bookYear": "1996", "bookAuthor": "au0", "bookPrice": 1000000, "bookAmount": 12},
    3:  {"bookID":3,  "bookNum": "book3",  "bookType": "Computer", "bookTitle": "Introduction to Data Science with C++", "bookPublisher": "pub0", "bookYear": "2018", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 9},
    4:  {"bookID":4,  "bookNum": "book4",  "bookType": "Computer", "bookTitle": "Introduction to OOP with Java",         "bookPublisher": "pub0", "bookYear": "2002", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 6},
    5:  {"bookID":5,  "bookNum": "book5",  "bookType": "Earth",    "bookTitle": "Cosmos",                                "bookPublisher": "pub0", "bookYear": "2018", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 8},
    6:  {"bookID":6,  "bookNum": "book6",  "bookType": "Magazine", "bookTitle": "Vorbes",                                "bookPublisher": "pub0", "bookYear": "2021", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 19},
    7:  {"bookID":7,  "bookNum": "book7",  "bookType": "Comic",    "bookTitle": "Naruto",                                "bookPublisher": "pub0", "bookYear": "2020", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 21},
    8:  {"bookID":8,  "bookNum": "book8",  "bookType": "Comic",    "bookTitle": "Jujutsu Kaisen",                        "bookPublisher": "pub0", "bookYear": "2020", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 10},
    9:  {"bookID":9,  "bookNum": "book9",  "bookType": "Earth",    "bookTitle": "National Geography",                    "bookPublisher": "pub0", "bookYear": "2021", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 1},
    10: {"bookID":10, "bookNum": "book10", "bookType": "History",  "bookTitle": "History of Human Beings",               "bookPublisher": "pub0", "bookYear": "1942", "bookAuthor": "au0", "bookPrice": 100000,  "bookAmount": 13},
}

book_operations = BookOperations(conn=conn, db=db)
for _, value in data_to_insert.items():
    book_operations.addBook(**value)
