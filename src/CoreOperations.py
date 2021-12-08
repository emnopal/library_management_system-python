import sys;sys.path.append('..')

from db.operations import Operations


class CoreOperations(Operations):

    SAFE_CREDENTIALS_TO_SHOW = "userID, username, fullName, phone, email"

    def __init__(self, conn, db, *args, **kwargs):
        super().__init__(conn=conn, db=db, *args, **kwargs)
        self.conn = conn
        self.db = db

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

    def addAdmin(
        self, userID, username, password,
        fullName="", phone="", email="", *args, **kwargs
    ):
        data = f"{userID}, '{username}', '{hash(password)}', '{fullName}', '{phone}', '{email}'"
        cols = "userID, username, password, fullName, phone, email"
        self.insert(table="admin", data=data, cols=cols, *args, **kwargs)

    def addRecord(
        self, recordID, bookID, cardID,
        borrowDate, returnDate, userID, *args, **kwargs
    ):

        data = f"'{recordID}', '{bookID}', '{cardID}', '{borrowDate}', '{returnDate}', '{userID}'"
        cols = "recordID, bookID, cardID, borrowDate, returnDate, userID"
        self.insert(table="record", data=data, cols=cols, *args, **kwargs)

    def addCard(
        self, cardID, cardNum, cardName,
        cardUnit, cardType, *args, **kwargs
    ):

        data = f"{cardID}, '{cardNum}', '{cardName}', '{cardUnit}', '{cardType}'"
        cols = "cardID, cardNum, cardName, cardUnit, cardType"
        self.insert(table="card", data=data, cols=cols, *args, **kwargs)

    def showCore(self, table, columns=None, *args, **kwargs):
        if table == "admin":
            return self.select(table="admin", columns=self.SAFE_CREDENTIALS_TO_SHOW)
        return self.select(table=table, columns=columns, *args, **kwargs)

    def searchCore(
        self, table, searchQuery=None, columnsToSearch=None,
        dataToSearch=None, columns=None, *args, **kwargs
    ):
        if table == "admin":
            if not searchQuery:
                if "password" in columnsToSearch:
                    raise ValueError("You can't search for password")
                searchQuery = f"{columnsToSearch}={dataToSearch}"
            else:
                if "password" in searchQuery:
                    raise ValueError("You can't search for password")
            return self.select(
                table="admin", columns=self.SAFE_CREDENTIALS_TO_SHOW,
                where=searchQuery, *args, **kwargs
            )

        else:
            if not searchQuery:
                searchQuery = f"{columnsToSearch}='{dataToSearch}'"
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
        getID = self.select(table=table, columns=f"{table}ID", where=deleteQuery, *args, **kwargs)[f"{table}ID"]

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


