from src.com.jalasoft.shoppingcar.db.product_query import SaleQuery


class CartSale:
    def __init__(self):
        print("cartSale class")

    def save_sale(self, sale):
        print(sale)
        query = SaleQuery()
        query.insert_sale(sale)

    def get_all_sales(self):
        query = SaleQuery()
        return query.load_all_sale()