from src.com.jalasoft.shoppingcar.view.home_view import HomeView
from src.com.jalasoft.shoppingcar.model.store_model import StoreModel
from src.com.jalasoft.shoppingcar.controller.CartController import ControllerStore

if __name__ == "__main__":
        view = HomeView()
        print("calling view")
        model = StoreModel()
        print("calling model")
        controller = ControllerStore(view, model)
        print("calling controller")
