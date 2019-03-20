
class Product(object):
    def __init__(self, id_product, name,  price):
        self.__id = id_product
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

