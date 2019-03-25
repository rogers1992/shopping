import sys

from PyQt5.QtWidgets import QApplication

from src.com.jalasoft.shoppingcar.view.home_view import HomeView
from src.com.jalasoft.shoppingcar.model.sale import Sale
from src.com.jalasoft.shoppingcar.controller.CartController import CartController

if __name__ == "__main__":
        app = QApplication(sys.argv)
        view = HomeView()
        print("calling view")
        model = Sale()
        print("calling model")
        controller = CartController(view, model)
        print("calling controller")
        sys.exit(app.exec_())
