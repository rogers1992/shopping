from src.com.jalasoft.shoppingcar.db.connection_db import ConnectionDB
from src.com.jalasoft.shoppingcar.model.sale import Sale


class ProductSales:
    def __init__(self):
        self.__conn = ConnectionDB().get_connection()

    def total_sale(self, sale: Sale):
        cursor = self.__conn.cursor()
        insert_sale = "insert into sales(total_price, date) values ('" + sale.calculate_price_total() + "'," "date('now'));"
        cursor.execute(insert_sale)
        self.__conn.commit()