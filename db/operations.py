from db.newDB import newDB

class Operations(newDB):

    def __init__(self, conn, db):
        super().__init__(conn=conn, database=db)

    def insert(self, table, cols=None, data=None, query=None, message=None):
        if not message:
            DEFAULT_INSERT_MSG = "Record inserted successfully"
        try:
            if not query:
                query = f"INSERT INTO {self.get_db_name()}.{table} ({cols}) VALUES ({data})"
            self.generate_query(query, DEFAULT_INSERT_MSG)
        except Exception as e:
            raise (e)

    def update(self, table, data=None, where=None, query=None, message=None):
        if not message:
            DEFAULT_UPDATE_MSG = "Record updated successfully"
        try:
            if not query:
                query = f"UPDATE {self.get_db_name()}.{table} SET {data} WHERE {where}"
            self.generate_query(query, DEFAULT_UPDATE_MSG)
        except Exception as e:
            raise (e)

    def delete(self, table, where=None, query=None, message=None):
        if not message:
            DEFAULT_DELETE_MSG = "Record deleted successfully"
        try:
            if not query:
                query = f"DELETE FROM {self.get_db_name()}.{table} WHERE {where}"
            self.generate_query(query, DEFAULT_DELETE_MSG)
        except Exception as e:
            raise (e)

    def select(self, table, where=None, query=None, message=None, columns=None):
        if not message:
            DEFAULT_SELECT_MSG = "Record selected successfully"
        try:
            if not query:
                if not columns:
                    if not where:
                        query = f"SELECT * FROM {self.get_db_name()}.{table}"
                    else:
                        query = f"SELECT * FROM {self.get_db_name()}.{table} WHERE {where}"
                else:
                    if not where:
                        query = f"SELECT {columns} FROM {self.get_db_name()}.{table}"
                    else:
                        query = f"SELECT {columns} FROM {self.get_db_name()}.{table} WHERE {where}"
            return list(self.generate_query(query, DEFAULT_SELECT_MSG).fetchall())
        except Exception as e:
            raise (e)

