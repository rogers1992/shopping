import os
import sqlite3


class ConnectionDB:
    dbName = "Shopping.db"

    def __init__(self):
        self.__exist = os.path.exists(self.dbName)

    def get_connection(self):
        conn = sqlite3.connect(self.dbName)
        c = conn.cursor()
        d = conn.cursor()
        e = conn.cursor()
        if not self.__exist:
            c.execute("CREATE TABLE IF NOT EXISTS product(id integer, name varchar(100), price real, primary key(id));"),
            d.execute("CREATE TABLE IF NOT EXISTS sales(id integer, total_sale float, date datetime, primary key(id));"),
            e.execute("CREATE TABLE IF NOT EXISTS prod_sales(id_prod integer , id_sales integer, quantity integer, FOREIGN KEY (id_prod) REFERENCES product(id), FOREIGN KEY (id_sales) REFERENCES sales(id);")

        return conn
