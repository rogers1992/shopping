import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic.properties import QtWidgets


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Shopping -  message'
        self.left = 0
        self.top = 0
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.question(self, 'message', "Thank you for placing your order.",
                                           QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            print('Ok clicked.')

        else:
            print('No clicked.')

        #self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())