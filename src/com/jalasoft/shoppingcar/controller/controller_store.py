from src.com.jalasoft.shoppingcar.view.home_view import HomeView
from src.com.jalasoft.shoppingcar.model.store_model import StoreModel


class ControllerStore:

    def __init__(self, view, model):
        print("controller")
        view.initUI()

