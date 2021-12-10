from datetime import datetime
from utils.checker import isNested, DatetimeConversion
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union, Tuple


# book table
class BookItem(BaseModel):
    bookID: int
    bookNum: Union[int, float, str]
    bookType: str
    bookTitle: str
    bookPublisher: str
    bookYear: Union[str, int]
    bookAuthor: str
    bookPrice: Union[int, float]
    bookAmount: int
    bookStock: int


# user table
class UserItem(BaseModel):
    userID: int
    username: str
    membership: str = "Member"
    name: str = ""


# record table
class RecordItem(BaseModel):
    recordID: int
    bookID: str
    userID: str
    borrowDate: Union[str, datetime] = datetime.now()
    returnDate: Union[str, datetime] = "0000-00-00 00:00:00"

    class Config:
        json_encoders = {
            datetime: DatetimeConversion
        }


