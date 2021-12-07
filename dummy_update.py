from db.connections import connections
from src.BookOperations import BookOperations

# set connection
conn, db = connections()

book_operations = BookOperations(conn=conn, db=db)
book_operations.updateBook(columnsToUpdate="bookAuthor", dataToUpdate="David J. Griffiths", columnsToSearch="bookTitle", dataToSearch="Introduction to Electrodynamics")