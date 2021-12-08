import os
from db.newDB import newDB
from dotenv import load_dotenv

load_dotenv()

host = os.environ['MYSQL_HOST']
user = os.environ['MYSQL_USERNAME']
db = os.environ['MYSQL_DATABASE']
pwd = os.environ['MYSQL_PWD']
port = os.environ['MYSQL_PORT']

def connections(
    host=host, user=user,
    db=db, pwd=pwd, port=port
):
    db_conn = newDB(
        host=host, user=user,
        database=db, password=pwd, port=port
    )

    return [
        db_conn.get_connections(), db_conn.get_db_name()
    ]

