from src.com.jalasoft.shoppingcar.model.product import Product


class Sale:
    def __init__(self):
        self.__product_list = []
        self.__total_price = None
        self.__sale_id = None
        self.__date = None

    def get_product_list(self):
        return self.__product_list

    def set_product_list(self, product_list):
        self.__product_list = product_list

    def get_total_price(self):
        return self.__total_price

    def set_total_price(self, total_price):
        self.__total_price = total_price

    def get_sale_id(self):
        return self.__sale_id

    def set_sale_id(self, sale_id):
        self.__sale_id = sale_id

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def add_product(self, product: Product):
        if self.is_product_in_list(product.get_id()):
            print("The product" + str(product.get_id()) + "exist!")
        else:
            self.__product_list.append(product)

    def remove_product(self, product: Product):
        if self.is_product_in_list(product.get_id()):
            self.__product_list.remove(product)
        else:
            print("The product" + str(product.get_id()) + "not exist!")

    def calculate_price_total(self):
        total_price = 0
        for product in self.__product_list:
            total_price += product.get_price()
        self.__total_price = total_price
        return self.__total_price

    def is_product_in_list(self, id_prod):
        for prod in self.__product_dict:
            if id_prod == prod.get_id():
                return True
