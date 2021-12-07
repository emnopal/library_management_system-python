import sys; sys.path.append('..')
from db.operations import Operations


class CardOperations(Operations):

    def __init__(self, conn, db, table="book"):
        super().__init__(conn=conn, db=db)
        self.table = table

    def addCard(self, cardID, cardNum, cardName, cardUnit, cardType):
        data = f"{cardID}, '{cardNum}', '{cardName}', '{cardUnit}', '{cardType}'"
        cols = "cardID, cardNum, cardName, cardUnit, cardType"
        self.insert(table=self.table, data=data, cols=cols)

    def showCard(self, columns=None):
        return self.select(table=self.table, columns=columns)

    def searchCard(self, searchQuery=None, columnsToSearch=None, dataToSearch=None, columns=None):
        if not searchQuery:
            searchQuery = f"{columnsToSearch}={dataToSearch}"
        return self.select(table=self.table, columns=columns, where=searchQuery)

    def updateCard(self, columnsToUpdate=None, dataToUpdate=None, columnsToSearch=None, dataToSearch=None, updateQuery=None, whereQuery=None):
        if not updateQuery:
            updateQuery = f"{columnsToUpdate}={dataToUpdate}"
        if not whereQuery:
            whereQuery = f"{columnsToSearch}={dataToSearch}"
        self.update(table=self.table, data=updateQuery, where=whereQuery)

    def deleteCard(self, columnsToDelete=None, dataToDelete=None, deleteQuery=None):
        if not deleteQuery:
            deleteQuery = f"{columnsToDelete}={dataToDelete}"
        self.delete(table=self.table, where=deleteQuery)
