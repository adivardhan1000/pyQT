import sys
from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "basicCalc.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.addNumbers.clicked.connect(self.add)
        self.subNumbers.clicked.connect(self.sub)
        self.mulNumbers.clicked.connect(self.mul)
        self.divNumbers.clicked.connect(self.mul)


    def add(self):
        number1 = int(self.number1.toPlainText())
        number2 = int(self.number2.toPlainText())
        solution = "The sum of two numbers is: " + str(number1+number2)
        self.answer.setText(solution)

    def sub(self):
        number1 = int(self.number1.toPlainText())
        number2 = int(self.number2.toPlainText())
        solution = "The subtraction of two numbers is: " + str(number1-number2)
        self.answer.setText(solution)

    def mul(self):
        number1 = int(self.number1.toPlainText())
        number2 = int(self.number2.toPlainText())
        solution = "The multiplication of two numbers is: " + str(number1*number2)
        self.answer.setText(solution)

    def div(self):
        number1 = int(self.number1.toPlainText())
        number2 = int(self.number2.toPlainText())
        solution = "The division of two numbers is: " + str(number1/number2)
        self.answer.setText(solution)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())