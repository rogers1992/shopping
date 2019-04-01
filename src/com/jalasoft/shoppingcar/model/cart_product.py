from src.com.jalasoft.shoppingcar.db.product_query import ProductQuery


class CartProduct:
    def __init__(self):
        print("cartProduct class")

    def save_product(self, product):
        print(product)
        query = ProductQuery()
        query.insert_product(product)

    def get_all_product(self):
        query = ProductQuery()
        return query.load_all_product()