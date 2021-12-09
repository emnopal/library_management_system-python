import sys;sys.path.append('..')
import re
import mysql.connector as mysql

from exceptions.exceptions import DatabaseConnectionError
from mysql.connector import Error, ProgrammingError


class newDB:

    DEFAULT_QUERY_MSG = "Query Executed"

    def __init__(
        self, host=None, user=None, password=None,
        database=None, port=None, conn=None, *args, **kwargs
    ):
        if conn:
            self.conn = conn
            self.database = database
        else:
            try:
                if database:
                    if port:
                        self.conn = mysql.connect(
                            host=host, user=user, password=password,
                            database=database, port=port, *args, **kwargs
                        )
                    self.conn = mysql.connect(
                        host=host, user=user, password=password,
                        database=database, *args, **kwargs
                    )
                    self.database = database
                else:
                    if port:
                        self.conn = mysql.connect(
                            host=host, user=user, password=password,
                            port=port, *args, **kwargs
                        )
                    self.conn = mysql.connect(
                        host=host, user=user, password=password,
                        *args, **kwargs
                    )
            except ProgrammingError:
                print(f"Database {database} not exists, creating...")
                if port:
                    self.conn = mysql.connect(
                        host=host, user=user, password=password,
                        port=port, *args, **kwargs
                    )
                self.conn = mysql.connect(
                    host=host, user=user, password=password,
                    *args, **kwargs
                )
                if database:
                    database = self.create_new_db(database, *args, **kwargs)
                    self.database = database
                    if port:
                        self.conn = mysql.connect(
                            host=host, user=user, password=password,
                            database=database, port=port, *args, **kwargs
                        )
                    self.conn = mysql.connect(
                        host=host, user=user, password=password,
                        database=database, *args, **kwargs
                    )
                    print(f"You're connected to database: {database}")
                else:
                    raise ValueError("Database name is required")
            except:
                raise DatabaseConnectionError(
                    "Error while connecting to database")

    def generate_query(
        self, query, message=DEFAULT_QUERY_MSG,
        *args, **kwargs
    ):
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor(dictionary=True, *args, **kwargs)
                cursor.execute(query)
                if bool(re.match(r"insert into|update|delete", query, re.IGNORECASE)):
                    self.conn.commit()
                    print(message)
                    return
                else:
                    print(message)
                    return cursor
        except Error as e:
            print("Error while connecting to MySQL", e)
        except Exception as e:
            print("Unexpected error: ", e)

    def create_new_db(self, db_name, *args, **kwargs):
        self.generate_query(
            f"CREATE DATABASE IF NOT EXISTS {db_name}",
            f"Database: {db_name} Created",
            *args, **kwargs
        )
        return db_name

    def create_new_table(self, table_name, columns_query, *args, **kwargs):
        if isinstance(columns_query, str):
            self.generate_query(
                f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_query})",
                f"Table: {table_name} Created",
                *args, **kwargs
            )
        if isinstance(columns_query, list):
            self.generate_query(
                f"CREATE TABLE IF NOT EXISTS {table_name} {tuple(columns_query)}",
                f"Table: {table_name} Created",
                *args, **kwargs
            )
        if isinstance(columns_query, tuple):
            self.generate_query(
                f"CREATE TABLE IF NOT EXISTS {table_name} {columns_query}",
                f"Table: {table_name} Created",
                *args, **kwargs
            )
        if isinstance(columns_query, dict):
            """
            For dict instance, key and value must be strings
            it's very usable for creating lot of table with lot of columns
            """
            for key, value in columns_query.items():
                self.generate_query(
                    f"CREATE TABLE IF NOT EXISTS {key} {value}",
                    f"Table: {key} Created",
                    *args, **kwargs
                )

    def get_connections(self):
        return self.conn

    def get_db_name(self):
        return self.database
