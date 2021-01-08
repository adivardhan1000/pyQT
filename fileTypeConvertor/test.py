from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
from pathlib import Path
import win32com.client
import os
from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)


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
        self.log.setText("Steps:")
        self.log.append("1. Select the files you want to convert")
        self.log.append("2. Enter the name for the output file")
        self.log.append("3. Select the destination folder")
        self.log.append("4. Select the operation you want to perform")
        self.log.append("(WARNING: Make sure you select correct file format else the program will exit)")
        self.log.append("5. Click on Convert and Save")
        self.log.append("Update Log:")

        
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
        self.log.append("Following files selected")
        for i in fname[0]:
            self.log.append(i) 
        #self.log.setText(fname[0])
        #self.convert.clicked.connect(self.check)

    def outputFolder(self):
        home_dir = str(Path.home())
        
        fname=QFileDialog.getExistingDirectory(self,"Choose Directory")
        #fname = QFileDialog.getOpenFileNames(self, 'Open file', home_dir)
        print(fname)
        self.log.append("Following folder path has been selected")
        self.log.append(fname)
        self.outputFileName = str(self.outputFileNameBox.toPlainText())
        print(self.outputFileName)
        self.outputPath = fname
        print(self.outputPath)
        
        
        #self.convert.clicked.connect(self.check)

    def check(self):
        if self.pptx2pdfO2O.isChecked():
            self.pptxtopdfO2O()
        elif self.docx2pdfO2O.isChecked():
            self.docxtopdfO2O()

        elif self.pdf2imgO2M.isChecked():
            self.pdftoimgO2M()

        elif self.img2pdfM2O.isChecked(): 
            self.imgtopdfM2O()
        elif self.pdf2pdfM2O.isChecked():
            self.pdftopdfM2O()
            
        elif self.image2pdfM2M.isChecked():
            self.imagetopdfM2M()
        elif self.pptx2pdfM2M.isChecked():
            self.pptxtopdfM2M()
        elif self.docx2pdfM2M.isChecked():
            self.docxtopdfM2M()
        
    #def pptxtopdfO2O(self):
    #    powerpoint = win32com.client.DispatchEx("Powerpoint.Application")
    #    powerpoint.Visible = 1
    #    outputFileName = str(self.outputPath)+"/"+str(self.outputFileName)+".pdf"
    #    deck = powerpoint.Presentations.Open(self.inputFiles[0])
    #    deck.SaveAs(outputFileName, 32) # formatType = 32 for ppt to pdf
    #    deck.Close()
    #    self.log.append("Succesfully converted to")
    #    self.log.append(outputFileName)
    #    powerpoint.Quit()



    def docxtopdfO2O(self):
        from docx2pdf import convert
        try:
            outputFile = str(self.outputPath)+"/"+str(self.outputFileName)+".pdf"
            convert(self.inputFiles[0], outputFile)
            self.log.append("Succesfully converted to")
            self.log.append(outputFile)
            print("converted")
        except AttributeError:
            self.log.append("Succesfully converted to")
            self.log.append(outputFile)
            pass

    def pdftoimgO2M(self):
        print('........................................................',self.inputFiles[0])
        images = convert_from_path(self.inputFiles[0],500)
        for i, image in enumerate(images):
            fname = "image" + str(i) + ".png"
            image.save(fname, "PNG")


    def imgtopdfM2O(self):
        import img2pdf
        outputFile = str(self.outputPath)+"/"+str(self.outputFileName)+".pdf"
        print(outputFile)
        with open(outputFile,"wb") as f:
	        f.write(img2pdf.convert(self.inputFiles))
        self.log.append("Succesfully converted to")
        self.log.append(outputFile)
        print("converted")

        
                


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()