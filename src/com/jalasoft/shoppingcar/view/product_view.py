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
        self.table = QTableWidget()
        #self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(4)
        self.table.setHorizontalHeaderLabels(["Id","Product", "Price", "Quantity"])

        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        """self.table.setItem(0, 0, QTableWidgetItem("0001"))
        self.table.setItem(0, 1, QTableWidgetItem("pants"))
        self.table.setItem(0, 2, QTableWidgetItem("50"))
        self.table.setItem(0, 3, QTableWidgetItem("1"))
        self.table.setItem(1, 0, QTableWidgetItem("0002"))
        self.table.setItem(1, 1, QTableWidgetItem("T-shirt"))
        self.table.setItem(1, 2, QTableWidgetItem("60"))
        self.table.setItem(1, 3, QTableWidgetItem("1"))

        self.table.setItem(2, 0, QTableWidgetItem("0003"))
        self.table.setItem(2, 1, QTableWidgetItem("Shoes"))
        self.table.setItem(2, 2, QTableWidgetItem("70"))
        self.table.setItem(2, 3, QTableWidgetItem("1"))

        self.table.setItem(3, 0, QTableWidgetItem("0004"))
        self.table.setItem(3, 1, QTableWidgetItem("Shirt"))
        self.table.setItem(3, 2, QTableWidgetItem("80"))
        self.table.setItem(3, 3, QTableWidgetItem("1"))"""

        self.table.move(0, 0)
        #group.setLayout(self.table)
        #self.tableWidget_2 = QtWidgets.QTableWidget(self.group)
        #number of the item
        self.table.doubleClicked.connect(self.numberItem)


        #self.table.changeEvent(self.numberItem())

        """form = QFormLayout()
        self.__productName = QLineEdit()
        form.addRow(QLabel("product Name"),self.__productName )
        form.addRow(QLabel("FileN"), QComboBox())
        form.addRow(QLabel("Ext"), QLineEdit())
        group.setLayout(form)"""

        buttonA = QPushButton("Add")

        self.table2 = QTableWidget()
        self.table2.setColumnCount(4)
        #self.table2.setRowCount(4)
        self.table2.setHorizontalHeaderLabels(["Id","Product", "Quantity","Price"])

        self.table2.setItem(0, 0, QTableWidgetItem("0001"))
        self.table2.setItem(0, 1, QTableWidgetItem("pants"))
        self.table2.setItem(0, 2, QTableWidgetItem("50"))
        self.table2.setItem(0, 3, QTableWidgetItem("1"))




        buttonC = QPushButton("Cancel")
        buttonF = QPushButton("Chek Out")


        #vLayout.addWidget(group)
        vLayout.addWidget(self.table)
        vLayout.addWidget(buttonA)
        vLayout.addWidget(self.table2)
        vLayout.addWidget(buttonC)
        vLayout.addWidget(buttonF)
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

    def getAddTocartButton(self):
        return self.buttonA