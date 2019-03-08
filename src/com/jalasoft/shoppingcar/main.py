from src.com.jalasoft.shoppingcar.view import home_view
from src.com.jalasoft.shoppingcar.model import store_model
from src.com.jalasoft.shoppingcar.controller import ccontroller_store

class Main:

    def __init__(self):
        view = HomeView()
        print("calling view")
        model = StoreModel()
        print("calling model")
        controller = ControllerStore(view, model)
        print("calling controller")
