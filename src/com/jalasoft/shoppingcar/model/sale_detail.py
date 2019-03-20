from src.com.jalasoft.shoppingcar.model.item import Item


class SaleDetail:

    def __init__(self, item_list: Item):
        self.__item_list = item_list
        self.__quantity = self.__item_list.count(self)

    def calculate_price_total(self):
        total = 0
        for item in self.__item_list:
            total += item.get_price()
        return total
