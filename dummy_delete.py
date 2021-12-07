from db.connections import connections
from src.BookOperations import BookOperations

# set connection
conn, db = connections()

book_operations = BookOperations(conn=conn, db=db)
book_operations.deleteBook(columnsToDelete="bookTitle", dataToDelete="Vorbes")