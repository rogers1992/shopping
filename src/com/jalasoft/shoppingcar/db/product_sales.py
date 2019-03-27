from src.com.jalasoft.shoppingcar.db.connection_db import ConnectionDB
from src.com.jalasoft.shoppingcar.model.sale import Sale


class ProductSales:
    def __init__(self):
        self.__conn = ConnectionDB().get_connection()

    def insert_sale(self, sale: Sale):
        cursor = self.__conn.cursor()
        insert_sale = "insert into sales(total_price, date) values ('" + sale.calculate_price_total() + "', date('now'));"
        cursor.execute(insert_sale)
        self.__conn.commit()
        #insert product_sale
        for prod in sale.get_product_list():
            insert_product_sale = "insert into prod_sales(id_prod, id_sales, quantity) values (" + prod.get_id() + ", (select max(id) from sales), " + prod.get_quantity() + ");"
            print(insert_product_sale)
            cursor.execute(insert_product_sale)
            self.__conn.commit()

    def load_all_sale(self):
        """TO DO, query to get all sales"""
        