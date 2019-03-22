from src.com.jalasoft.shoppingcar.model.product import Product


class SaleDetail:

    def __init__(self, product_list: Product):
        self.__product_list = product_list
        self.__quantity = self.__product_list.count(self)

    def calculate_price_total(self):
        total = 0
        for product in self.__product_list:
            total += product.get_price()
        return total
