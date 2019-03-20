from src.com.jalasoft.shoppingcar.db.product_query import ProductQuery

class Sale:
    def __init__(self):
        self.__product_list = {}

    def add_product(self, product):
        self.__product_list[product.get_id()] = product

    def save_product(self, product):
        print(product)
        query = ProductQuery()
        query.insertProduct(product)

    def remove_product(self, id_product):
        for key, value in dict(self.__product_list).items():
            if key == id_product:
                del self.__product_list[id_product]

    def get_product_all(self):
        return self.__product_list

    def get_all_product(self):
        query = ProductQuery()
        return query.loadAllProduct()
