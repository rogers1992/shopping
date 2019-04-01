from src.com.jalasoft.shoppingcar.db.connection_db import ConnectionDB
from src.com.jalasoft.shoppingcar.model.sale import Sale


class ProductSales:
    def __init__(self):
        self.__conn = ConnectionDB().get_connection()

    "Insertion the Sale on DB"

    def insert_sale(self, sale: Sale):
        cursor = self.__conn.cursor()
        insert_sale = "insert into sales(total_price, date) values ('" + sale.calculate_price_total() + "', date('now'));"
        cursor.execute(insert_sale)
        self.__conn.commit()
        # insert product_sale
        for prod in sale.get_product_list():
            insert_product_sale = "insert into prod_sales(id_prod, id_sales, quantity) values (" + prod.get_id() + ", (select max(id) from sales), " + prod.get_quantity() + ");"
            print(insert_product_sale)
            cursor.execute(insert_product_sale)
            self.__conn.commit()

    "Loading all the Sales from DB"

    def load_all_sale(self):
        """TO DO, query to get all sales"""
        cursor = self.__conn.cursor()
        cursor.execute("select id, total_price, date from sales;")
        row_sales = cursor.fetchall()
        salesList = []
        for row in row_sales:
            sale = Sale()
            sale.set_sale_id(row[0])
            sale.set_total_price(row[1])
            sale.set_date(row[2])
            salesList.append(sale)

        return salesList
