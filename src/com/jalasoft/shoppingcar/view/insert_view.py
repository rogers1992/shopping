from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton


class InsertView(QWidget):
#class ProductInsertView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()

        group = QGroupBox()
        form = QFormLayout()
        self.name = QLineEdit()
        self.price = QLineEdit()
        self.quantity = QLineEdit()
        form.addRow(QLabel("Product Name:"), self.name)
        form.addRow(QLabel("Produt Price:"), self.price)
        form.addRow(QLabel("Quantity:"), self.quantity)
        group.setLayout(form)

        self.saveButton = QPushButton("Save Product", self)

        vLayout.addWidget(group)
        vLayout.addWidget(self.saveButton)
        self.setLayout(vLayout)

    def getSaveProductButton(self):
        return self.saveButton

    def getName(self):
        return self.name.text()

    def getPrice(self):
        return self.price.text()

    def getQuantity(self):
        return self.quantity.text()
