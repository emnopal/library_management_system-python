import time; import sys; sys.path.append('..')
from CoreOperations import CoreOperations

class ChildOperations(CoreOperations):

    def __init__(self, conn, db, *args, **kwargs):
        super().__init__(conn=conn, db=db, *args, **kwargs)
        self.conn = conn
        self.db = db

    def addBookStock(
        self, bookStock, bookID=None, bookNum=None,
        *args, **kwargs
    ):
        if not bookID:
            bookID = self.searchCore(
                table="book", columnsToSearch="bookID",
                dataToSearch=bookNum, *args, **kwargs)[0]["bookID"]

        self.updateCore(
            table="book", updateQuery=f"bookStock = bookStock + {bookStock}",
            whereQuery=f"bookID = {bookID}", *args, **kwargs)

    def borrowBook(
        self, cardID, bookNum,
        userID, recordID,
        *args, **kwargs
    ):
        result = self.searchCore(
            table="book", columnsToSearch="bookNum", dataToSearch=bookNum,
            columns="bookID, bookStock", *args, **kwargs)[0]

        if result["bookStock"] == 0:
            stockResult = self.searchCore(
                table="record", searchQuery=f'bookID = {result["bookID"]} ORDER BY returnDate DESC',
                columns='returnDate', *args, **kwargs
            )
            return stockResult[0]["returnDate"]

        self.updateCore(
            table="book", updateQuery=f'bookStock = {result["bookStock"]} - 1',
            whereQuery="bookNum = {bookNum}", *args, **kwargs
        )

        self.addRecord(
            recordID=recordID, bookID=result["bookID"], cardID=cardID,
            userID=userID, returnDate=None, borrowDate=time.strftime('%Y-%m-%d %H:%M:%S'),
            *args, **kwargs
        )

    def returnBook(self, cardID, bookNum, *args, **kwargs):
        bookID = self.searchCore(
            table="book", columnsToSearch="bookNum",
            dataToSearch=bookNum, columns="bookID", *args, **kwargs)[0]['bookID']

        recordID = self.searchCore(
            table="record", searchQuery=f'bookID = {bookID} AND cardID = {cardID} AND returnDate IS NULL',
            columns='recordID', *args, **kwargs)[0]['recordID']

        self.updateCore(
            table="record", updateQuery=f'returnDate = "{time.strftime("%Y-%m-%d %H:%M:%S")}"',
            whereQuery=f'recordID = {recordID}', *args, **kwargs
        )

        stockUpdate = self.searchCore(
            columnsToSearch="bookID", dataToSearch=bookID,
            columns="bookStock", *args, **kwargs)[0]['bookStock']

        self.updateCore(
            table="book", updateQuery=f'bookStock = {stockUpdate} + 1',
            whereQuery=f'bookNum = {bookNum}', *args, **kwargs
        )

    def checkAdmin(self, username, *args, **kwargs):
        return self.searchCore(
            table="admin", columnsToSearch="username",
            dataToSearch=username, *args, **kwargs
        )

    def queryBookByUser(self, cardNum, *args, **kwargs):

        cardID = self.searchCore(
            table="card", columnsToSearch="cardNum", dataToSearch=cardNum,
            columns="cardID", *args, **kwargs)[0]['cardID']

        return self.joinCore(
            table="book", tableToJoin="record", on="book.bookID = record.bookID",
            whereQuery=f"cardID={cardID} AND return_date IS NULL", *args, **kwargs
        )

    def queryBookList(self, searchQuery=None, colsToQuery=None, value=None, *args, **kwargs):

        if not searchQuery:
            searchQuery = f"{colsToQuery} LIKE '%{value}%'"
            if colsToQuery == "bookYear":
                if "-" in value:
                    value = value.split("-")
                    searchQuery = f"bookYear BETWEEN '{value[0]}' AND '{value[1]}'"
                searchQuery = f"bookYear == '{value}'"
            if colsToQuery == "bookPrice":
                if "-" in value:
                    value = value.split("-")
                    searchQuery = f"bookPrice BETWEEN '{value[0]}' AND '{value[1]}'"
                searchQuery = f"bookPrice == '{value}'"

        appendedSearchQuery = ""
        if isinstance(searchQuery, dict):
            for key, value in searchQuery.items():
                appendedSearchQuery += f"AND {key} LIKE '%{value}%'"
                if key == "bookYear":
                    if "-" in value:
                        value = value.split("-")
                        appendedSearchQuery += f" AND bookYear BETWEEN '{value[0]}' AND '{value[1]}'"
                    appendedSearchQuery += f" AND bookYear == '{value}'"
                elif key == "bookPrice":
                    if "-" in value:
                        value = value.split("-")
                        appendedSearchQuery += f" AND bookPrice BETWEEN '{value[0]}' AND '{value[1]}'"
                    appendedSearchQuery += f" AND bookPrice == '{value}'"
            appendedSearchQuery = appendedSearchQuery[4:]
            return self.searchCore(table="book", searchQuery=appendedSearchQuery, *args, **kwargs)

        return self.searchCore(table="book", searchQuery=searchQuery, *args, **kwargs)

