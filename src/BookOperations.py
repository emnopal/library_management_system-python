import sys; sys.path.append('..')
from db.operations import Operations


class BookOperations(Operations):

    def __init__(self, conn, db, table="book"):
        super().__init__(conn=conn, db=db)
        self.table = table

    def addBook(self, bookID, bookNum, bookType, bookTitle, bookPublisher, bookYear, bookAuthor, bookPrice, bookAmount, bookStock=None):
        if not bookStock:
            bookStock = bookAmount
        data = f"{bookID}, '{bookNum}', '{bookType}', '{bookTitle}', '{bookPublisher}', '{bookYear}', '{bookAuthor}', {bookPrice}, {bookAmount}, {bookStock}"
        cols = "bookID, bookNum, bookType, bookTitle, bookPublisher, bookYear, bookAuthor, bookPrice, bookAmount, bookStock"
        self.insert(table=self.table, data=data, cols=cols)

    def showBook(self, columns=None):
        return self.select(table=self.table, columns=columns)

    def searchBook(self, searchQuery=None, columnsToSearch=None, dataToSearch=None, columns=None):
        if not searchQuery:
            searchQuery = f"{columnsToSearch}='{dataToSearch}'"
        return self.select(table=self.table, columns=columns, where=searchQuery)

    def updateBook(self, columnsToUpdate=None, dataToUpdate=None, columnsToSearch=None, dataToSearch=None, updateQuery=None, whereQuery=None):
        if not updateQuery:
            updateQuery = f"{columnsToUpdate}='{dataToUpdate}'"
        if not whereQuery:
            whereQuery = f"{columnsToSearch}='{dataToSearch}'"
        self.update(table=self.table, data=updateQuery, where=whereQuery)

    def deleteBook(self, columnsToDelete=None, dataToDelete=None, deleteQuery=None):
        if not deleteQuery:
            deleteQuery = f"{columnsToDelete}='{dataToDelete}'"
        self.delete(table=self.table, where=deleteQuery)
