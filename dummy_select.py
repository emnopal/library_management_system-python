from db.connections import connections
from src.CoreOperations import CoreOperations
from src.ChildOperations import ChildOperations

# set connection
conn, db = connections()

operations = CoreOperations(conn=conn, db=db)
new_ops = ChildOperations(conn=conn, db=db)

print(operations.searchCore(table="book", columnsToSearch="bookNum", dataToSearch="book1", columns="bookStock, bookID"))
print(operations.searchCore(table="book", columnsToSearch="bookTitle", dataToSearch="Introduction to Electrodynamics"))
print(new_ops.queryBookByUser(userID=1))
print(new_ops.listOfAvailableBooks())
print(list(new_ops.getBookID(bookTitle="National Geography", columns="bookID, bookStock").values())[0])
print(new_ops.getBookID(bookNum="book1"))
print(operations.showCore(table="record"))
print(new_ops.checkUser(name="Husein"))
print(new_ops.checkUser(username="cd01"))
print(new_ops.queryBookByUser(name="Husein"))