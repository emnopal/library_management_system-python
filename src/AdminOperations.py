import sys; sys.path.append('..')
from db.operations import Operations


class AdminOperations(Operations):

    SAFE_CREDENTIALS_TO_SHOW = "userID, username, fullName, phone, email"

    def __init__(self, conn, db, table="book"):
        super().__init__(conn=conn, db=db)
        self.table = table

    def addAdmin(self, userID, username, password, fullName="", phone="", email=""):
        data = f"{userID}, '{username}', '{hash(password)}', '{fullName}', '{phone}', '{email}'"
        cols = "userID, username, password, fullName, phone, email"
        self.insert(table=self.table, data=data, cols=cols)

    def showAdmin(self):
        return self.select(table=self.table, columns=self.SAFE_CREDENTIALS_TO_SHOW)

    def searchAdmin(self, searchQuery=None, columnsToSearch=None, dataToSearch=None):
        if not searchQuery:
            if "password" in columnsToSearch:
                raise ValueError("You can't search for password")
            searchQuery = f"{columnsToSearch}={dataToSearch}"
        else:
            if "password" in searchQuery:
                raise ValueError("You can't search for password")
        return self.select(table=self.table, columns=self.SAFE_CREDENTIALS_TO_SHOW, where=searchQuery)

    def updateAdmin(self, columnsToUpdate=None, dataToUpdate=None, columnsToSearch=None, dataToSearch=None, updateQuery=None, whereQuery=None):
        if not updateQuery:
            updateQuery = f"{columnsToUpdate}={dataToUpdate}"
        if not whereQuery:
            whereQuery = f"{columnsToSearch}={dataToSearch}"
        self.update(table=self.table, data=updateQuery, where=whereQuery)

    def deleteAdmin(self, columnsToDelete=None, dataToDelete=None, deleteQuery=None):
        if not deleteQuery:
            deleteQuery = f"{columnsToDelete}={dataToDelete}"
        self.delete(table=self.table, where=deleteQuery)
