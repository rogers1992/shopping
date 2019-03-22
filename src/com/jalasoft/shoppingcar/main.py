import sys

from PyQt5.QtWidgets import QApplication

from src.com.jalasoft.shoppingcar.view.home_view import HomeView
from src.com.jalasoft.shoppingcar.model.store_model import StoreModel
from src.com.jalasoft.shoppingcar.controller.controller_store import ControllerStore

if __name__ == "__main__":
        app = QApplication(sys.argv)
        view = HomeView()
        print("calling view")
        sys.exit(app.exec_())
        model = StoreModel()
        print("calling model")
        controller = ControllerStore(view, model)
        print("calling controller")
