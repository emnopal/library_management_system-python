import sys; sys.path.append('..')

import mysql.connector as mysql
import re

from mysql.connector import Error, ProgrammingError

from exceptions.exceptions import DatabaseConnectionError

class newDB:

    DEFAULT_QUERY_MSG = "Query Executed"

    def __init__(self, host=None, user=None, password=None, database=None, port=None, conn=None):
        if conn:
            self.conn = conn
            self.database = database
        else:
            try:
                if database:
                    if port:
                        self.conn = mysql.connect(host=host, user=user, password=password, database=database, port=port)
                    self.conn = mysql.connect(host=host, user=user, password=password, database=database)
                    self.database = database
                else:
                    if port:
                        self.conn = mysql.connect(host=host, user=user, password=password, port=port)
                    self.conn = mysql.connect(host=host, user=user, password=password)
            except ProgrammingError:
                print(f"Database {database} not exists, creating...")
                if port:
                    self.conn = mysql.connect(host=host, user=user, password=password, port=port)
                self.conn = mysql.connect(host=host, user=user, password=password)
                if database:
                    database = self.create_new_db(database)
                    self.database = database
                    if port:
                        self.conn = mysql.connect(host=host, user=user, password=password, database=database, port=port)
                    self.conn = mysql.connect(host=host, user=user, password=password, database=database)
                    print(f"You're connected to database: {database}")
                else:
                    raise ValueError("Database name is required")
            except:
                raise DatabaseConnectionError("Error while connecting to database")

    def generate_query(self, query, message=DEFAULT_QUERY_MSG):
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()
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

    def create_new_db(self, db_name):
        self.generate_query(f"CREATE DATABASE IF NOT EXISTS {db_name}", f"Database: {db_name} Created")
        return db_name

    def create_new_table(self, table_name, columns_query):
        if isinstance(columns_query, str):
            self.generate_query(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_query})", f"Table: {table_name} Created")
        if isinstance(columns_query, list):
            self.generate_query(f"CREATE TABLE IF NOT EXISTS {table_name} {tuple(columns_query)}", f"Table: {table_name} Created")
        if isinstance(columns_query, tuple):
            self.generate_query(f"CREATE TABLE IF NOT EXISTS {table_name} {columns_query}", f"Table: {table_name} Created")

    def get_connections(self):
        return self.conn

    def get_db_name(self):
        return self.database

