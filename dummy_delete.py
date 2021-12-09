from db.connections import connections
from src.CoreOperations import CoreOperations
from src.ChildOperations import ChildOperations

# set connection
conn, db = connections()

del_operations = CoreOperations(conn=conn, db=db)
del_operations.deleteCore(table='book', columnsToDelete="bookTitle", dataToDelete="Vorbes")