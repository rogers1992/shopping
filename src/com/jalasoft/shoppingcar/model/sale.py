
class Sale:
    def __init__(self):
        self.__item_list = []

    def add_item(self, item):
        self.__item_list.append(item)

    def remove_item(self, item):
        self.remove_item(item)

    def get_item_all(self):
        return self.__item_list
