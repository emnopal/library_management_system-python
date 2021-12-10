import sys;sys.path.append('..')

from db.operations import Operations


class CoreModels(Operations):

    def __init__(self, conn, db, *args, **kwargs):
        super().__init__(conn=conn, db=db, *args, **kwargs)

    def addBook(
        self, bookID, bookNum, bookType, bookTitle, bookPublisher,
        bookYear, bookAuthor, bookPrice, bookAmount, bookStock=None,
        *args, **kwargs
    ):
        if not bookStock:
            bookStock = bookAmount
        data = f"{bookID}, '{bookNum}', '{bookType}', '{bookTitle}', '{bookPublisher}', '{bookYear}', '{bookAuthor}', {bookPrice}, {bookAmount}, {bookStock}"
        cols = "bookID, bookNum, bookType, bookTitle, bookPublisher, bookYear, bookAuthor, bookPrice, bookAmount, bookStock"
        self.insert(table="book", data=data, cols=cols, *args, **kwargs)

    def addUser(
        self, userID, username, membership="Member",
        name="", *args, **kwargs
    ):
        data = f"{userID}, '{username}', '{name}', '{membership}'"
        cols = "userID, username, name, membership"
        self.insert(table="user", data=data, cols=cols, *args, **kwargs)

    def addRecord(
        self, recordID, bookID, borrowDate,
        userID, returnDate=None, *args, **kwargs
    ):
        if not returnDate:
            data = f"'{recordID}', '{bookID}', '{borrowDate}', '0000-00-00 00:00:00', '{userID}'"
        else:
            data = f"'{recordID}', '{bookID}', '{borrowDate}', '{returnDate}', '{userID}'"
        cols = "recordID, bookID, borrowDate, returnDate, userID"
        self.insert(table="record", data=data, cols=cols, *args, **kwargs)

    def showCore(self, table, columns=None, *args, **kwargs):
        return self.select(table=table, columns=columns, *args, **kwargs)

    def searchCore(
        self, table, searchQuery=None, columnsToSearch=None,
        dataToSearch=None, columns=None, *args, **kwargs
    ):
        if not searchQuery:
            searchQuery = f"{columnsToSearch}='{dataToSearch}'"
        return self.select(
            table=table, columns=columns,
            where=searchQuery, *args, **kwargs
        )

    def searchLikeCore(
        self, table, searchQuery=None, columnsToSearch=None,
        dataToSearch=None, columns=None, *args, **kwargs
    ):
        if not searchQuery:
            searchQuery = f"{columnsToSearch} LIKE '{dataToSearch}'"
        return self.select(
            table=table, columns=columns,
            where=searchQuery, *args, **kwargs
        )

    def updateCore(
        self, table, columnsToUpdate=None, dataToUpdate=None, columnsToSearch=None,
        dataToSearch=None, updateQuery=None, whereQuery=None, *args, **kwargs
    ):
        if not updateQuery:
            updateQuery = f"{columnsToUpdate}='{dataToUpdate}'"
        if not whereQuery:
            whereQuery = f"{columnsToSearch}='{dataToSearch}'"
        self.update(table=table, data=updateQuery,
                    where=whereQuery, *args, **kwargs)

    def deleteCore(self, table, columnsToDelete=None, dataToDelete=None, deleteQuery=None, *args, **kwargs):
        if not deleteQuery:
            deleteQuery = f"{columnsToDelete}='{dataToDelete}'"
        self.delete(table=table, where=deleteQuery, *args, **kwargs)
        try:
            getID = self.select(table=table, columns=f"{table}ID", where=deleteQuery, *args, **kwargs)[f"{table}ID"]
        except:
            return "No data!"

        deleteRecord = f"{table}ID = '{getID}'"
        self.delete(table="record", where=deleteRecord, *args, **kwargs)

    def joinCore(
        self, table, tableToJoin, on, searchQuery=None, columnsToSearch=None,
        dataToSearch=None, joinQuery="JOIN", columns=None, *args, **kwargs
    ):
        if not searchQuery:
            searchQuery = f"{columnsToSearch}='{dataToSearch}'"
        return self.selectJoin(
            table=table, tableToJoin=tableToJoin, on=on, joinQuery=joinQuery,
            columns=columns, where=searchQuery, *args, **kwargs
        )


