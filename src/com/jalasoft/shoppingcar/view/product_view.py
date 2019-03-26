from PyQt5.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QMenu, QMainWindow, QPushButton, QGroupBox, \
    QVBoxLayout, QComboBox, QTableWidget, QCheckBox, QHBoxLayout, QTableWidgetItem, QAbstractItemView
#from src.com.jalasoft.shoppingcar.view.check_out_view import CheckOut
from PyQt5.uic.properties import QtWidgets


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.intUI()

    def intUI(self):
        print("aqui")

        vLayout = QVBoxLayout()




        #group = QGroupBox()


        #check = QCheckBox(self)
        #check.toggle()


        #cb = QCheckBox('Show title', self)
        self.table = QTableWidget()# table of Product
        #self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        #self.table.setRowCount()
        self.table.setHorizontalHeaderLabels(["Id","Product", "Price", "Quantity"])

        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.table.move(0, 0)
        #group.setLayout(self.table)
        #self.tableWidget_2 = QtWidgets.QTableWidget(self.group)
        #number of the item
        self.table.doubleClicked.connect(self.numberItem)


        #self.table.changeEvent(self.numberItem())

        buttonAdd = QPushButton("Add") #button Add

        self.table2 = QTableWidget() #table of shopping Cart
        self.table2.setColumnCount(4)
        self.table2.setHorizontalHeaderLabels(["Id","Product", "Quantity","Price"])

        buttonCan = QPushButton("Cancel")
        buttonCO = QPushButton("Chek Out")


        #vLayout.addWidget(group)
        vLayout.addWidget(self.table)
        vLayout.addWidget(buttonAdd)
        vLayout.addWidget(self.table2)
        vLayout.addWidget(buttonCan)
        vLayout.addWidget(buttonCO)
        self.setLayout(vLayout)



    def getTable(self):
        return self.table
    def getProductName(self):
        return self.__productName.text()
    def numberItem(self):
        print("\n")
        for currentQTableWidgetItem in self.table.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    def getCartTable(self):
        return self.table2

    def getAddTocartButton(self): #add product to shopping Cart
        return self.buttonAdd

    def getSaveButton(self): #Create shopping Cart
        return self.buttonCO

    def getCancelButton(self): #Clear shopping Cart
        return self.buttonCan