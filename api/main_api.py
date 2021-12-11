import sys; sys.path.append('..')
from fastapi import FastAPI
from src.CoreModels import CoreModels
from src.ChildModels import ChildModels
from db.connections import connections
from utils.checker import isNested
from api.datatype_validation import *
from api.app_api import *

app = FastAPI()
conn, db = connections()
coreOps = CoreModels(conn=conn, db=db)
childOps = ChildModels(conn=conn, db=db)


# [C]reate or insert
# for book table
@app.post("/api/add/book")
async def add_to_book(item: BookItem):
    if isNested(item):
        for _, value in item.items():
            coreOps.addBook(**value)
    else:
        coreOps.addBook(**item)

# for user table
@app.post("/api/add/user/")
async def add_to_user(item: UserItem):
    if isNested(item):
        for _, value in item.items():
            coreOps.addUser(**value)
    else:
        coreOps.addUser(**item)

# for record table
@app.post("/api/add/record/")
async def add_to_record(item: RecordItem):
    if isNested(item):
        for _, value in item.items():
            coreOps.addRecord(**value)
    else:
        coreOps.addRecord(**item)


# [R]ead
# show all table
@app.get("/api/get/all/")
async def get_all():
    return coreOps.showCore(table="book")

@app.get("/api/get/all/{table}/")
async def get_all(table: str):
    return coreOps.showCore(table=table)

@app.get("/api/get/all/book/title/{titlename}/")
async def get_all_book_title(titlename: str):
    return coreOps.searchLikeCore(table="book", columnsToSearch="bookTitle", dataToSearch=titlename)

@app.get("/api/get/all/book/available/")
async def get_all_book_available():
    return childOps.listOfAvailableBooks()

@app.get("/api/get/book/num/{bookNum}/")
async def get_book_by_id(bookNum: str):
    return childOps.getBookID(bookNum=bookNum)

# BEGIN TODO: check function here!

@app.get("/api/get/book/title/{bookTitle}/")
async def get_book_by_id(bookTitle: str):
    return childOps.getBookID(bookTitle=bookTitle)

@app.get("/api/get/user/username/{username}/")
async def get_user_by_name(username: str):
    return childOps.checkUser(username=username)

@app.get("/api/get/user/name/{name}/")
async def get_user_by_name(name: str):
    return childOps.checkUser(name=name)

@app.get("/api/get/user/{userID}/")
@app.get("/api/get/user/id/{userID}/")
async def get_user_by_id(userID: int):
    return childOps.getNameFromID(userID=userID)

@app.get("/api/get/book/user/borrowed/")
async def get_book_borrowed():
    return childOps.userWhoBorrowedBook()

@app.get("/api/get/book/user/{userID}/")
@app.get("/api/get/book/user/id/{userID}/")
async def get_user_by_name(userID: int):
    return childOps.queryBookByUser(userID=userID)

@app.get("/api/get/book/user/name/{name}/")
async def get_user_by_name(name: str):
    return childOps.queryBookByUser(name=name)

@app.get("/api/get/book/user/username/{username}/")
async def get_user_by_name(username: str):
    return childOps.queryBookByUser(username=username)

# END TODO!


# [U]pdate
@app.put("/api/add/book/stock/{stockToAdd}/id/{bookID}/")
@app.put("/api/add/book/stock/{stockToAdd}/{bookID}/")
async def add_book_to_stock(stockToAdd: int, bookID: int):
    childOps.addBookToStock(stockToAdd=stockToAdd, bookID=bookID)

@app.put("/api/add/book/stock/{stockToAdd}/title/{bookTitle}/")
async def add_book_to_stock(stockToAdd: int, bookTitle: str):
    childOps.addBookToStock(stockToAdd=stockToAdd, bookTitle=bookTitle)

@app.put("/api/add/book/stock/{stockToAdd}/num/{bookNum}/")
async def add_book_to_stock(stockToAdd: int, bookNum: Union[int, str, float]):
    childOps.addBookToStock(stockToAdd=stockToAdd, bookNum=bookNum)

# borrow book
@app.put("/api/borrow/{recordID}/{userID}/{bookID}/")
@app.put("/api/borrow/{recordID}/{userID}/id/{bookID}/")
async def borrow_book(userID: int, recordID: int, bookID: int):
    childOps.borrowBook(userID=userID, recordID=recordID, bookID=bookID)

@app.put("/api/borrow/{recordID}/{userID}/title/{bookTitle}/")
async def borrow_book(userID: int, recordID: int, bookTitle: str):
    childOps.borrowBook(userID=userID, recordID=recordID, bookTitle=bookTitle)

@app.put("/api/borrow/{recordID}/{userID}/num/{bookNum}/")
async def borrow_book(userID: int, recordID: int, bookNum: Union[int, str, float]):
    childOps.borrowBook(userID=userID, recordID=recordID, bookNum=bookNum)

# return book
@app.put("/api/return/{userID}/title/{bookTitle}/")
async def return_book(userID: int, bookTitle: str):
    childOps.returnBook(userID=userID, bookTitle=bookTitle)

@app.put("/api/return/{userID}/num/{bookNum}/")
async def return_book(userID: int, bookNum: Union[int, str, float]):
    childOps.returnBook(userID=userID, bookNum=bookNum)

@app.put("/api/return/{userID}/{bookID}")
@app.put("/api/return/{userID}/id/{bookID}")
async def return_book(userID: int, bookID: int):
    childOps.returnBook(userID=userID, bookID=bookID)

# change membership
@app.put("/api/update/user/membership/username/{username}/{membership}/")
async def update_membership(username: str, membership: str):
    childOps.changeMembership(username=username, membership=membership)

@app.put("/api/update/user/membership/name/{name}/{membership}/")
async def update_membership(name: str, membership: str):
    childOps.changeMembership(name=name, membership=membership)

@app.put("/api/update/user/membership/{userID}/{membership}/")
@app.put("/api/update/user/membership/id/{userID}/{membership}/")
async def update_membership(userID: int, membership: str):
    childOps.changeMembership(userID=userID, membership=membership)


# [D]elete
# book
@app.delete("/api/delete/book/{bookID}/")
@app.delete("/api/delete/book/id/{bookID}/")
async def delete_book(bookID: Union[int, str, float]):
    try:
        coreOps.deleteCore(table="book", columnsToDelete="bookID", dataToDelete=bookID)
    except:
        try:
            coreOps.deleteCore(table="book", columnsToDelete="bookNum", dataToDelete=bookID)
        except:
            return {"message": "book not found"}

@app.delete("/api/delete/book/title/{bookTitle}/")
async def delete_book_title(bookTitle: str):
    coreOps.deleteCore(table="book", columnsToDelete="bookTitle", dataToDelete=bookTitle)

@app.delete("/api/delete/user/{userID}/")
@app.delete("/api/delete/user/id/{userID}/")
async def delete_user(userID: int):
    coreOps.deleteCore(table="user", columnsToDelete="userID", dataToDelete=userID)

# user
@app.delete("/api/delete/user/username/{username}/")
async def delete_username(username: str):
    coreOps.deleteCore(table="user", columnsToDelete="username", dataToDelete=username)

@app.delete("/api/delete/user/name/{name}/")
async def delete_name(name: str):
    coreOps.deleteCore(table="user", columnsToDelete="name", dataToDelete=name)

#record
@app.delete("/api/delete/record/{recordID}/")
@app.delete("/api/delete/record/id/{recordID}/")
async def delete_record(recordID: int):
    coreOps.deleteCore(table="record", columnsToDelete="recordID", dataToDelete=recordID)
