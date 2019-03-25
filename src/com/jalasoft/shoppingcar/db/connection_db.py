import os
import sqlite3


class ConnectionDB:
    dbName = "Shopping.db"

    def __init__(self):
        self.__exist = os.path.exists(self.dbName)

    def get_connection(self):
        conn = sqlite3.connect(self.dbName)
        c = conn.cursor()
        if not self.__exist:
            c.execute("CREATE TABLE IF NOT EXISTS PRODUCT(id integer, name varchar(100), price real, primary key(id));")

        return conn