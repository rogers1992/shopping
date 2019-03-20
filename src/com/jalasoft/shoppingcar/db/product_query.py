from src.com.jalasoft.shoppingcar.db.connection_db import ConnectionDB
from src.com.jalasoft.shoppingcar.model.product import Product


class ProductQuery:
    def __init__(self):
        self.__conn = ConnectionDB().getConnection()

    def insertProduct(self, product):
        cursor = self.__conn.cursor()
        insertQuery = "insert into product(id, name, price) values ('" + Product.get_id() + "', '" + Product.get_name() + "'," + str(
            Product.get_price()) + ");"
        print(insertQuery)
        cursor.execute(insertQuery)
        self.__conn.commit()

    def loadAllProduct(self):
        cursor = self.__conn.cursor()
        cursor.execute("select name, price from product;")
        rows = cursor.fetchall()
        productList = []
        for row in rows:
            prod = Product()
            prod.setProductName(row[0])
            prod.setProductPrice(row[1])
            productList.append(prod)

        return productList
