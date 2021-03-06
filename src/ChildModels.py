from collections import defaultdict
import time; import sys; sys.path.append('..')
from src.CoreModels import CoreModels

class ChildModels(CoreModels):

    def __init__(self, conn, db, *args, **kwargs):
        super().__init__(conn=conn, db=db, *args, **kwargs)

    def getBookID(self, bookTitle=None, bookNum=None, columns="bookID", *args, **kwargs):
        if bookTitle:
            bookID = self.searchLikeCore(
                table="book", columnsToSearch="bookTitle",
                dataToSearch=bookTitle, columns=columns, *args, **kwargs)#[0]
        else:
            bookID = self.searchLikeCore(
                table="book", columnsToSearch="bookNum",
                dataToSearch=bookNum, columns=columns, *args, **kwargs)[0]
        return bookID

    def addBookStock(
        self, stockToAdd, bookTitle=None, bookID=None, bookNum=None,
        *args, **kwargs
    ):
        if not bookID:
            bookID = self.getBookID(bookTitle=bookTitle,bookNum=bookNum, *args, **kwargs)["bookID"]
        self.updateCore(
            table="book", updateQuery=f"bookStock = bookStock + {stockToAdd}",
            whereQuery=f"bookID = {bookID}", *args, **kwargs)
        self.updateCore(
            table="book", updateQuery=f"bookAmount = bookAmount + {stockToAdd}",
            whereQuery=f"bookID = {bookID}", *args, **kwargs)
        return

    def borrowBook(
        self, userID, recordID,
        bookNum=None, bookTitle=None, bookID=None,
        *args, **kwargs
    ):
        if not bookID:
            bookID, bookStock = list(self.getBookID(
                bookTitle=bookTitle,bookNum=bookNum,
                columns="bookID, bookStock", *args, **kwargs).values())
        else:
            bookStock = self.searchCore(
                table="book", columns="bookStock",
                columnsToSearch="bookID", dataToSearch=bookID, *args, **kwargs)[0]['bookStock']
        if bookStock == 0:
            stockResult = self.searchCore(
                table="record", searchQuery=f'bookID = {bookID} ORDER BY returnDate DESC',
                columns='returnDate', *args, **kwargs
            )
            return stockResult[0]["returnDate"]
        self.updateCore(
            table="book", updateQuery=f'bookStock = {bookStock} - 1',
            whereQuery=f"bookID = {bookID}", *args, **kwargs
        )
        self.addRecord(
            recordID=recordID, bookID=bookID, userID=userID,
            borrowDate=time.strftime('%Y-%m-%d %H:%M:%S'),
            returnDate=None,
            *args, **kwargs
        )
        return

    def returnBook(
        self, userID,
        bookNum=None, bookTitle=None, bookID=None,
        *args, **kwargs):
        if not bookID:
            bookID = self.getBookID(
                bookTitle=bookTitle, bookNum=bookNum,
                columns="bookID", *args, **kwargs)["bookID"]
        recordID = self.searchCore(
            table="record", searchQuery=f"bookID = {bookID} AND userID = {userID} AND returnDate='0000-00-00 00:00:00'",
            columns='recordID', *args, **kwargs)[0]['recordID']
        self.updateCore(
            table="record", updateQuery=f'returnDate = "{time.strftime("%Y-%m-%d %H:%M:%S")}"',
            whereQuery=f'recordID = {recordID}', *args, **kwargs
        )
        stockUpdate = self.searchCore(
            columnsToSearch="bookID", dataToSearch=bookID, table="book",
            columns="bookStock", *args, **kwargs)[0]['bookStock']
        self.updateCore(
            table="book", updateQuery=f'bookStock = {stockUpdate} + 1',
            whereQuery=f'bookID = {bookID}', *args, **kwargs
        )
        return

    def checkUser(self, username=None, name=None, *args, **kwargs):
        if name:
            return self.searchLikeCore(
                table="user", columnsToSearch="name",
                dataToSearch=name, *args, **kwargs
            )
        if username:
            return self.searchLikeCore(
                table="user", columnsToSearch="username",
                dataToSearch=username, *args, **kwargs
            )
        if username != None and name != None:
            return self.searchLikeCore(table="user", columnsToSearch="username",
                dataToSearch=username, *args, **kwargs
            )
        else:
            raise ValueError("No username or name provided")

    def queryBookByUser(self, userID=None, username=None, name=None, *args, **kwargs):
        if not userID:
            userID = self.checkUser(username=username, name=name)[0]['userID']
        return self.joinCore(
            table="book", tableToJoin="record", on="book.bookID = record.bookID",
            searchQuery=f"userID={userID} AND returnDate='0000-00-00 00:00:00'", *args, **kwargs
        )

    def getNameFromID(self, userID, *args, **kwargs):
        return self.searchCore(
            table="user", columnsToSearch="userID",
            dataToSearch=userID, columns="username", *args, **kwargs
        )[0]['username']

    def userWhoBorrowedBook(self, *args, **kwargs):
        borrowedBook = self.joinCore(
            table="book", tableToJoin="record", on="book.bookID = record.bookID",
            searchQuery=f"returnDate='0000-00-00 00:00:00'", *args, **kwargs
        )
        listofBook = defaultdict(list)
        for queries in range(len(borrowedBook)):
            listofBook[borrowedBook[queries]['bookTitle']].append(self.getNameFromID(borrowedBook[queries]['userID']))
        return listofBook

    def listOfAvailableBooks(self, *args, **kwargs):
        available_book = self.searchCore(
            table="book", searchQuery="bookStock > 0", *args, **kwargs
        )
        listBook = {}
        for queries in range(len(available_book)):
            listBook[available_book[queries]['bookTitle']] = available_book[queries]['bookStock']
        return listBook

    def changeMembership(self, membership, username=None, name=None, userID=None, *args, **kwargs):
        if not userID:
            userID = self.checkUser(username=username, name=name)[0]['userID']
        self.updateCore(
            table="user", updateQuery=f"membership = '{membership}'",
            whereQuery=f"userID = {userID}", *args, **kwargs
        )

    def queryBookList(self, searchQuery=None, colsToQuery=None, value=None, *args, **kwargs):
        # TODO: test this method, or review maybe this method duplicated with other method!!!
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

