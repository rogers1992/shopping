
class Product(object):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__price = None

    def get_id(self):
        return self.__id

    def set_id(self, id_product):
        self.__id = id_product

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

