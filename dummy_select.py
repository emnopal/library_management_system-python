from db.connections import connections
from src.ChildModels import ChildModels
from src.CoreModels import CoreModels

# set connection
conn, db = connections()

operations = CoreModels(conn=conn, db=db)
new_ops = ChildModels(conn=conn, db=db)

print(operations.searchCore(table="book", columnsToSearch="bookNum", dataToSearch="book1", columns="bookStock, bookID"))
print(operations.searchCore(table="book", columnsToSearch="bookTitle", dataToSearch="Introduction to Electrodynamics"))
print(new_ops.queryBookByUser(userID=1))
print(new_ops.listOfAvailableBooks())
print(list(new_ops.getBookID(bookTitle="National Geography", columns="bookID, bookStock")[0].values())[0])
print(new_ops.getBookID(bookNum="book1"))
print(new_ops.getBookID(bookTitle="quantum"))
print(operations.showCore(table="record"))
print(new_ops.checkUser(name="Husein"))
print(new_ops.checkUser(username="cd01"))
print(new_ops.queryBookByUser(name="Husein"))

