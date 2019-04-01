from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, \
    QComboBox, QTableWidget, QTableWidgetItem, QAbstractItemView, QPlainTextEdit
import sys

class OrderView(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Shopping - Order'
        self.initUI()

    def initUI(self):
        self.initComponent()

    def initComponent(self):
        vLayout = QVBoxLayout()

        self.tableOrder = QTableWidget(self)
        self.tableOrder.setColumnCount(3)
        self.tableOrder.setHorizontalHeaderLabels(["ID", "Product Name", "Price"])

        self.textTotal = QPlainTextEdit(self)
        self.textTotal.setPlainText("Total:")

        self.okButton = QPushButton("OK", self)

        vLayout.addWidget(self.tableOrder)
        vLayout.addWidget(self.self.textTotal)
        vLayout.addWidget(self.okButton)

        self.setLayout(vLayout)

    def getTableOrder(self):
        return self.tableOrder

    def getOkButton(self):
        return self.okButton


