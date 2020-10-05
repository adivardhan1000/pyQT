from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
from pathlib import Path


pyQTfileName = "fileBrowser.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(pyQTfileName)

class Example(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        #self.textEdit = QTextEdit()
        #self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.outputFileNameBox.setText("coverted")
        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        #openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.showDialog)
        self.browseButton.clicked.connect(self.showDialog)
        self.outputFolderBrowse.clicked.connect(self.outputFolder)
        self.convert.clicked.connect(self.check)

        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(openFile)

        #self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        home_dir = str(Path.home())
        
        #fname=QFileDialog.getExistingDirectory(self,"Choose Directory","E:\\")
        fname = QFileDialog.getOpenFileNames(self, 'Open file', home_dir)
        print(fname)
        if len(fname[0]) == 1:
            self.filePath.setText(fname[0][0])
        else:
            self.filePath.setText(str(len(fname[0]))+" files selected")
        self.inputFiles = fname[0]
        #self.convert.clicked.connect(self.check)

    def outputFolder(self):
        home_dir = str(Path.home())
        
        fname=QFileDialog.getExistingDirectory(self,"Choose Directory")
        #fname = QFileDialog.getOpenFileNames(self, 'Open file', home_dir)
        print(fname)
        outputFileName = str(self.outputFileNameBox.toPlainText())
        print(outputFileName)
        outputPath = fname
        print(outputPath)
        self.outputFile = str(outputPath)+"/"+str(outputFileName)+".pdf"
        print(self.outputFile)
        #self.convert.clicked.connect(self.check)

    def check(self):
        if self.image2pdf.isChecked(): 
            self.img2pdf()
            
    def img2pdf(self):
        import img2pdf
        print(self.outputFile)
        with open(self.outputFile,"wb") as f:
	        f.write(img2pdf.convert(self.inputFiles))
            
        print("converted")

        
                


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()