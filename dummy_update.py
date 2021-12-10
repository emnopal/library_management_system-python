from db.connections import connections
from src.ChildModels import ChildModels
from src.CoreModels import CoreModels

# set connection
conn, db = connections()

operations = CoreModels(conn=conn, db=db)
new_ops = ChildModels(conn=conn, db=db)

operations.updateCore(
    table="book",
    columnsToUpdate="bookAuthor",
    dataToUpdate="David J. Griffiths",
    columnsToSearch="bookTitle",
    dataToSearch="Introduction to Electrodynamics"
)

new_ops.changeMembership(name="Husein", membership="Member Plus")