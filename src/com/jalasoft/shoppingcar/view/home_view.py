from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QMenu, QMainWindow, QPushButton, QGroupBox, \
    QVBoxLayout, QComboBox, QAction
from src.com.jalasoft.shoppingcar.view.product_view import ProductView
from src.com.jalasoft.shoppingcar.view.menu_product_view import ProductShowView
from src.com.jalasoft.shoppingcar.view.insert_view import InsertView
from PyQt5.QtCore import Qt


class HomeView(QMainWindow):
    def __init__(self):

        super().__init__()
        self.title = 'Shopping - Product'
        self.left = 0
        self.top = 0
        self.width = 535
        self.height = 500
        #self.initUI()

    def initUI(self, controller):
    #def initUI(self, controller):
        #self.__controller = controller      incluye el controlador
        self.__controller = controller
        print("iniui")

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.__initComponet()

        self.show()

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

    def __initComponet(self):
        print("com")

        menuBar = self.menuBar()
        prodOption = menuBar.addMenu("Register")

        productMenu = QMenu("Product", self)
        prodOption.addMenu(productMenu)

        """shoppingCardOption = QAction("Shopping Card", self)
        shopOption.addAction(shoppingCardOption)"""
        self.loadShoppingCardView()
        self.__controller.loadProduct()

        insertOption = QAction("Insert", self)
        productMenu.addAction(insertOption)
        showOption = QAction("Show", self)
        productMenu.addAction(showOption)

        #insertOption.triggered.connect(lambda: self.loadInsertView())
        insertOption.triggered.connect(lambda: self.loadInsertView())
        showOption.triggered.connect(lambda: self.loadProductShowView())

        #showOption.triggered.connect(lambda: self.loadMenuProduct())
        #shoppingCardOption.triggered.connect(lambda: self.loadShoppingCardView())


        #self.setCentralWidget(self.__getProductView())
        #self.setsetDownWidget(self.__getCheckOut())

    def __getProductView(self):
        print("prod")
        self.proView = ProductView()
        return self.proView
        #self.__controller.addActionListener()

    def loadProductShowView(self):
        self.setCentralWidget(ProductView())
        self.__controller.loadProduct()
        #self.__controller.addActionListener()

    def loadInsertView(self):
        self.setCentralWidget(InsertView())
        self.__controller.addActionListener()
        print("clicked new product")

    def loadShoppingCardView(self):
        self.setCentralWidget(self.__getProductView())
        #self.__controller.addActionListener()

    def loadMenuProduct(self):
        self.setCentralWidget(self.ProductShowView())
        #self.__controller.addActionListener()

    def getTableProduct(self):
        return self.proView.getTable()

    def getShowOption(self):
        return self.showOption

class QtableWidget(object):
    pass
