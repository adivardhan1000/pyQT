import sys
from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap



pyQTfileName = "fileBrowser.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(pyQTfileName)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        self.browseButton.clicked.connect(self.browse)
    
    def browse(self):
        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        #openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.showDialog)
        #fileMenu.addAction(openFile)

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())