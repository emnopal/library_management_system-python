from db.connections import connections
from src.CoreOperations import CoreOperations

# set connection
conn, db = connections()

# insert into book
bookInsert = {
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

user = {
    1:  {"userID":1,  "username": "cd01",  "name": "Abdul",  "membership": "Member"},
    2:  {"userID":2,  "username": "cd02",  "name": "Husein", "membership": "Member"},
    3:  {"userID":3,  "username": "cd03",  "name": "Ali",    "membership": "Member"},
}

records = {
    1:  {"recordID":1,  "bookID": 1,  "userID": 1, "borrowDate": "2021-11-06 07:10:11", "returnDate":"2021-12-03 10:12:30"},
    2:  {"recordID":2,  "bookID": 1,  "userID": 2, "borrowDate": "2021-11-06 08:12:30", "returnDate":"2021-12-06 11:21:14"},
    3:  {"recordID":3,  "bookID": 1,  "userID": 3, "borrowDate": "2021-11-06 09:14:40", "returnDate":"2021-11-23 11:59:31"},
    4:  {"recordID":4,  "bookID": 2,  "userID": 2, "borrowDate": "2021-11-07 07:11:50", "returnDate":"2021-11-25 11:17:36"},
    5:  {"recordID":5,  "bookID": 3,  "userID": 1, "borrowDate": "2021-11-07 07:17:20", "returnDate":"0000-00-00 00:00:00"},
    6:  {"recordID":6,  "bookID": 5,  "userID": 3, "borrowDate": "2021-11-07 08:13:40", "returnDate":"2021-12-01 11:11:10"},
    7:  {"recordID":7,  "bookID": 7,  "userID": 2, "borrowDate": "2021-11-08 09:19:30", "returnDate":"2021-12-03 13:15:52"},
    8:  {"recordID":8,  "bookID": 9,  "userID": 1, "borrowDate": "2021-11-08 10:20:02", "returnDate":"0000-00-00 00:00:00"},
    9:  {"recordID":9,  "bookID": 9,  "userID": 3, "borrowDate": "2021-11-08 11:11:01", "returnDate":"0000-00-00 00:00:00"},
    10: {"recordID":10, "bookID": 7,  "userID": 1, "borrowDate": "2021-11-08 10:20:10", "returnDate":"2021-11-28 10:41:11"},
}

operations = CoreOperations(conn=conn, db=db)
for _, value in bookInsert.items():
    operations.addBook(**value)

for _, value in user.items():
    operations.addUser(**value)

for _, value in records.items():
    operations.addRecord(**value)