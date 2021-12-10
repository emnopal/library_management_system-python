from db.connections import connections
from src.CoreOperations import CoreOperations
from src.ChildOperations import ChildOperations

# set connection
conn, db = connections()

del_operations = CoreOperations(conn=conn, db=db)

#del_operations.deleteCore(table='record', deleteQuery="recordID = 15 AND recordID = 16 AND recordID = 17") # not works, i'm working on it

# currently work option
del_operations.deleteCore(table='book', columnsToDelete="bookTitle", dataToDelete="Vorbes")
del_operations.deleteCore(table='record', columnsToDelete="recordID", dataToDelete="15")
del_operations.deleteCore(table='record', columnsToDelete="recordID", dataToDelete="16")
del_operations.deleteCore(table='record', columnsToDelete="recordID", dataToDelete="17")