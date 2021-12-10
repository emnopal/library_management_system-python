from db.connections import connections
from src.CoreOperations import CoreOperations
from src.ChildOperations import ChildOperations

# set connection
conn, db = connections()

operations = CoreOperations(conn=conn, db=db)
new_ops = ChildOperations(conn=conn, db=db)

"""operations.updateCore(
    table="book",
    columnsToUpdate="bookAuthor",
    dataToUpdate="David J. Griffiths",
    columnsToSearch="bookTitle",
    dataToSearch="Introduction to Electrodynamics"
)"""

new_ops.changeMembership(name="Husein", membership="Member Plus")