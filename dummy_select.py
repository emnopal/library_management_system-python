from db.connections import connections
from src.CoreOperations import CoreOperations

# set connection
conn, db = connections()

operations = CoreOperations(conn=conn, db=db)
#print(book_operations.showBook())
print(operations.searchCore(table="book", columnsToSearch="bookNum", dataToSearch="book1", columns="bookStock, bookID"))