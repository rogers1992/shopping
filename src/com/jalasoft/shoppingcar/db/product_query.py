from src.com.jalasoft.shoppingcar.db.connection_db import ConnectionDB
from src.com.jalasoft.shoppingcar.model.product import Product


class ProductQuery:
    def __init__(self):
        self.__conn = ConnectionDB().get_connection()

    def insert_product(self, product):
        cursor = self.__conn.cursor()
        insertQuery = "insert into product(id, name, price) values ('" + str(product.get_id()) + "', '" + product.get_name() + "'," + str(
            str(product.get_price())) + ");"
        print(insertQuery)
        cursor.execute(insertQuery)
        self.__conn.commit()

    def load_all_product(self):
        cursor = self.__conn.cursor()
        cursor.execute("select id, name, price from product;")
        rows = cursor.fetchall()
        productList = []
        for row in rows:
            prod = Product()
            prod.set_id(row[0])
            prod.set_name(row[1])
            prod.set_price(row[2])
            productList.append(prod)

        return productList
