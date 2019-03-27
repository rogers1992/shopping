from src.com.jalasoft.shoppingcar.db.product_sales import ProductSales


class CartSale:
    def __init__(self):
        print("cartSale class")

    def save_sale(self, sale):
        print(sale)
        query = ProductSales()
        query.insert_sale(sale)

    def get_all_sales(self):
        query = ProductSales()
        return query.load_all_sale()


