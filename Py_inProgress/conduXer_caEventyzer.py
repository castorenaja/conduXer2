# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer_caEventyzer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageSequence
import os.path

class Ui_caEventWindow(object):
    def setupCaEventUi(self, caEventWindow):
        caEventWindow.setObjectName("caEventWindow")
        caEventWindow.resize(935, 655)
        self.centralwidget = QtWidgets.QWidget(caEventWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(20, 20, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(25)
        self.titleLabel.setFont(font)
        self.titleLabel.setAutoFillBackground(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.inputFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputFileLabel.setGeometry(QtCore.QRect(29, 352, 171, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.inputFileLabel.setFont(font)
        self.inputFileLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputFileLabel.setObjectName("inputFileLabel")
        self.inputFileEntry = QtWidgets.QListWidget(self.centralwidget)
        self.inputFileEntry.setGeometry(QtCore.QRect(200, 340, 571, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputFileEntry.sizePolicy().hasHeightForWidth())
        self.inputFileEntry.setSizePolicy(sizePolicy)
        self.inputFileEntry.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.inputFileEntry.setFont(font)
        self.inputFileEntry.setLineWidth(1)
        self.inputFileEntry.setIconSize(QtCore.QSize(0, 0))
        self.inputFileEntry.setResizeMode(QtWidgets.QListView.Fixed)
        self.inputFileEntry.setGridSize(QtCore.QSize(0, 0))
        self.inputFileEntry.setBatchSize(100)
        self.inputFileEntry.setObjectName("inputFileEntry")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(780, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.fpsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsLabel.setGeometry(QtCore.QRect(30, 490, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fpsEntry.setGeometry(QtCore.QRect(200, 480, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fpsEntry.sizePolicy().hasHeightForWidth())
        self.fpsEntry.setSizePolicy(sizePolicy)
        self.fpsEntry.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.fpsEntry.setFont(font)
        self.fpsEntry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fpsEntry.setCursorPosition(2)
        self.fpsEntry.setObjectName("fpsEntry")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(720, 540, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fluo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.displayFramesOpt = QtWidgets.QSlider(self.centralwidget)
        self.displayFramesOpt.setGeometry(QtCore.QRect(570, 480, 71, 41))
        self.displayFramesOpt.setMaximum(1)
        self.displayFramesOpt.setSliderPosition(0)
        self.displayFramesOpt.setOrientation(QtCore.Qt.Horizontal)
        self.displayFramesOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.displayFramesOpt.setObjectName("displayFramesOpt")
        self.dispOptNot = QtWidgets.QLabel(self.centralwidget)
        self.dispOptNot.setGeometry(QtCore.QRect(550, 450, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptNot.setFont(font)
        self.dispOptNot.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptNot.setObjectName("dispOptNot")
        self.dispOptYes = QtWidgets.QLabel(self.centralwidget)
        self.dispOptYes.setGeometry(QtCore.QRect(620, 450, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptYes.setFont(font)
        self.dispOptYes.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptYes.setObjectName("dispOptYes")
        self.displayFramesLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayFramesLabel.setGeometry(QtCore.QRect(380, 490, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.displayFramesLabel.setFont(font)
        self.displayFramesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.displayFramesLabel.setObjectName("displayFramesLabel")
        self.inputMaskLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputMaskLabel.setGeometry(QtCore.QRect(29, 412, 151, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.inputMaskLabel.setFont(font)
        self.inputMaskLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputMaskLabel.setObjectName("inputMaskLabel")
        self.inputMaskEntry = QtWidgets.QListWidget(self.centralwidget)
        self.inputMaskEntry.setGeometry(QtCore.QRect(200, 400, 571, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputMaskEntry.sizePolicy().hasHeightForWidth())
        self.inputMaskEntry.setSizePolicy(sizePolicy)
        self.inputMaskEntry.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.inputMaskEntry.setFont(font)
        self.inputMaskEntry.setLineWidth(1)
        self.inputMaskEntry.setIconSize(QtCore.QSize(0, 0))
        self.inputMaskEntry.setResizeMode(QtWidgets.QListView.Fixed)
        self.inputMaskEntry.setGridSize(QtCore.QSize(0, 0))
        self.inputMaskEntry.setBatchSize(100)
        self.inputMaskEntry.setObjectName("inputMaskEntry")
        self.browseButtonMask = QtWidgets.QPushButton(self.centralwidget)
        self.browseButtonMask.setGeometry(QtCore.QRect(780, 400, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.browseButtonMask.setFont(font)
        self.browseButtonMask.setObjectName("browseButtonMask")
        self.inputFileLabel.raise_()
        self.inputFileEntry.raise_()
        self.browseButton.raise_()
        self.fpsLabel.raise_()
        self.fpsEntry.raise_()
        self.runButton.raise_()
        self.label.raise_()
        self.titleLabel.raise_()
        self.displayFramesOpt.raise_()
        self.dispOptNot.raise_()
        self.dispOptYes.raise_()
        self.displayFramesLabel.raise_()
        self.inputMaskLabel.raise_()
        self.inputMaskEntry.raise_()
        self.browseButtonMask.raise_()
        caEventWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(caEventWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 21))
        self.menubar.setObjectName("menubar")
        caEventWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(caEventWindow)
        self.statusbar.setObjectName("statusbar")
        caEventWindow.setStatusBar(self.statusbar)

        self.retranslateUi(caEventWindow)
        QtCore.QMetaObject.connectSlotsByName(caEventWindow)

# Added ================       
 
        self.initiateWidgets()

# =====================

    def retranslateUi(self, caEventWindow):
        _translate = QtCore.QCoreApplication.translate
        caEventWindow.setWindowTitle(_translate("caEventWindow", "MainWindow"))
        self.titleLabel.setText(_translate("caEventWindow", "conduXer2:Intracellular Ca2+ Event Analysis"))
        self.inputFileLabel.setText(_translate("caEventWindow", "Input Video Stack:"))
        self.browseButton.setText(_translate("caEventWindow", "Browse"))
        self.fpsLabel.setText(_translate("caEventWindow", "Frame Rate (fps):"))
        self.fpsEntry.setText(_translate("caEventWindow", "30"))
        self.runButton.setText(_translate("caEventWindow", "RUN"))
        self.dispOptNot.setText(_translate("caEventWindow", "No"))
        self.dispOptYes.setText(_translate("caEventWindow", "Yes"))
        self.displayFramesLabel.setText(_translate("caEventWindow", "Display Frames?"))
        self.inputMaskLabel.setText(_translate("caEventWindow", "Input Mask File:"))
        self.browseButtonMask.setText(_translate("caEventWindow", "Browse"))

# Added ====================

    def initiateWidgets(self):
        self.browseButton.clicked.connect(self.openFileBrowser)
        self.browseButtonMask.clicked.connect(self.openMaskBrowser)
        self.runButton.clicked.connect(self.mainCaEventyzerFunction)

    def openFileBrowser(self):   
        global inFile
        options = QtWidgets.QFileDialog.Options()
        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Fluorescence TIF-Stack File", "", "TIF Files (*.tif)", options=options)
        if inFile:
            print(inFile)
        self.inputFileEntry.addItem(inFile)
        del options

    def openMaskBrowser(self):   
        global maskFile
        options = QtWidgets.QFileDialog.Options()
        maskFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Fluorescence TIF-Stack File", "", "TIF Files (*.tif)", options=options)
        if maskFile:
            print(maskFile)
        self.inputMaskEntry.addItem(maskFile)
        del options
    
    def mainCaEventyzerFunction(self):      
        
        global fps, fSp, cid, currCoords, roiCoords, fourierOption, displayOption, resampleFactor, directory, rootVideoName      
        
        fps = int(self.fpsEntry.text())
        displayOption = self.displayFramesOpt.value()    

        self.caEventyzer(inFile, fps, maskFile)
        
    def caEventyzer(self, inStack,fps,maskFile):
        
        imgMask = cv2.imread(maskFile) # 1:Color, 0:Grayscale, -1:Unchaged
        myMaskImg = cv2.cvtColor(imgMask, cv2.COLOR_BGR2GRAY)
        retGray, threshGray = cv2.threshold(myMaskImg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # Use THRESH_BINARY_INV if the background is white
        contours, hierarchy = cv2.findContours(threshGray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        cntAreas = np.zeros(len(contours),dtype='uint32')   
    
        for p in range(0,len(contours)):
            cntAreas[p] = cv2.contourArea(contours[p])
    
        tupleIndexes = np.where(cntAreas>99)
        arrIndexes = list(tupleIndexes[0])
    
        selectContours = list( contours[i] for i in arrIndexes)
        numCnts = len(selectContours)
        print numCnts
        
        stackName = inStack.split("/")[-1]
        directory = inStack[:-len(stackName)]+'/'+stackName[:-4]
        rootStackName = stackName[:-4]
    
        if not os.path.exists(directory):
            os.makedirs(directory)
              
        try:
            myStack = Image.open(inStack)
        except:
            print 'Error Loading Stack File'



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    caEventWindow = QtWidgets.QMainWindow()
    ui = caEventWindow()
    ui.setupcaEventUi(caEventWindow)
    caEventWindow.show()
    sys.exit(app.exec_())

