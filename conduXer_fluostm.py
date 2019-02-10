# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer_fluostm.ui'
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

class Ui_fluoWindow(object):
    def setupFluoUi(self, fluoWindow):
        fluoWindow.setObjectName("fluoWindow")
        fluoWindow.resize(935, 595)
        self.centralwidget = QtWidgets.QWidget(fluoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(20, 20, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(25)
        self.titleLabel.setFont(font)
        self.titleLabel.setAutoFillBackground(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.inputFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputFileLabel.setGeometry(QtCore.QRect(29, 352, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.inputFileLabel.setFont(font)
        self.inputFileLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputFileLabel.setObjectName("inputFileLabel")
        self.inputFileEntry = QtWidgets.QListWidget(self.centralwidget)
        self.inputFileEntry.setGeometry(QtCore.QRect(130, 340, 641, 41))
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
        self.fpsLabel.setGeometry(QtCore.QRect(30, 430, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fpsEntry.setGeometry(QtCore.QRect(200, 420, 141, 41))
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
        self.runButton.setGeometry(QtCore.QRect(720, 480, 191, 71))
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
        self.displayFramesOpt.setGeometry(QtCore.QRect(570, 420, 71, 41))
        self.displayFramesOpt.setMaximum(1)
        self.displayFramesOpt.setSliderPosition(0)
        self.displayFramesOpt.setOrientation(QtCore.Qt.Horizontal)
        self.displayFramesOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.displayFramesOpt.setObjectName("displayFramesOpt")
        self.dispOptNot = QtWidgets.QLabel(self.centralwidget)
        self.dispOptNot.setGeometry(QtCore.QRect(550, 390, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptNot.setFont(font)
        self.dispOptNot.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptNot.setObjectName("dispOptNot")
        self.dispOptYes = QtWidgets.QLabel(self.centralwidget)
        self.dispOptYes.setGeometry(QtCore.QRect(620, 390, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptYes.setFont(font)
        self.dispOptYes.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptYes.setObjectName("dispOptYes")
        self.displayFramesLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayFramesLabel.setGeometry(QtCore.QRect(380, 430, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.displayFramesLabel.setFont(font)
        self.displayFramesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.displayFramesLabel.setObjectName("displayFramesLabel")
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
        fluoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fluoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 21))
        self.menubar.setObjectName("menubar")
        fluoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fluoWindow)
        self.statusbar.setObjectName("statusbar")
        fluoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(fluoWindow)
        QtCore.QMetaObject.connectSlotsByName(fluoWindow)
        
# Added ================       
 
        self.initiateWidgets()

# =====================
        

    def retranslateUi(self, fluoWindow):
        _translate = QtCore.QCoreApplication.translate
        fluoWindow.setWindowTitle(_translate("fluoWindow", "MainWindow"))
        self.titleLabel.setText(_translate("fluoWindow", "conduXer<sup>2</sup>: Fluorescence Line-Scan"))
        self.inputFileLabel.setText(_translate("fluoWindow", "Input File:"))
        self.browseButton.setText(_translate("fluoWindow", "Browse"))
        self.fpsLabel.setText(_translate("fluoWindow", "Frame Rate (fps):"))
        self.fpsEntry.setText(_translate("fluoWindow", "30"))
        self.runButton.setText(_translate("fluoWindow", "RUN"))
        self.dispOptNot.setText(_translate("fluoWindow", "No"))
        self.dispOptYes.setText(_translate("fluoWindow", "Yes"))
        self.displayFramesLabel.setText(_translate("fluoWindow", "Display Frames?"))

 # Added ===========
        
    def initiateWidgets(self):
        self.browseButton.clicked.connect(self.openFileBrowser)
        self.runButton.clicked.connect(self.mainFluoFunction)

    def openFileBrowser(self):   
        global inFile
        options = QtWidgets.QFileDialog.Options()
#        options |= QtWidgets.QFileDialog.DontUseNativeDialog
#        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select STM File", "", "TIFF Files (*.tif *.png)", options=options)
        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Fluorescence TIF-Stack File", "", "TIF Files (*.tif)", options=options)
        if inFile:
            print(inFile)
        self.inputFileEntry.addItem(inFile)
        del options

    def mainFluoFunction(self):      
        
        global fps, fSp, cid, currCoords, roiCoords, fourierOption, displayOption, resampleFactor, directory, rootVideoName      
        
        fps = int(self.fpsEntry.text())
        displayOption = self.displayFramesOpt.value()
        
        self.fluoStackReader(inFile, fps)
        
        plt.show()
        
        
    def fluoStackReader(self, inStack,fps):
        
        stackName = inStack.split("/")[-1]
        directory = inStack[:-len(stackName)]+'/'+stackName[:-4]
        rootStackName = stackName[:-4]
    
        if not os.path.exists(directory):
            os.makedirs(directory)
              
        try:
            myStack = Image.open(inStack)
        except:
            print 'Error Loading Stack File'

        countOpt = 0
        counter = 0

        while countOpt == 0:
            try:
                myStack.seek(counter)
                counter = counter+1
            except:
                countOpt = 1
            
        numFrames = counter

        sumMaxFrame = np.zeros(np.array(myStack).shape)
        
        for frame in ImageSequence.Iterator(myStack):
            npFrame = np.array(frame,np.uint16)
            sumMaxFrame = sumMaxFrame + npFrame
            
        normMaxFrame = ((np.amax(sumMaxFrame)-sumMaxFrame)/np.amax(sumMaxFrame))*255.
        thMaxFrame = cv2.adaptiveThreshold(normMaxFrame.astype(dtype='uint8'), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 55, 1)
        unoTh = thMaxFrame/255   

        medianArray = np.zeros(numFrames,dtype=int)
        
        cntFr = 0
        for frame in ImageSequence.Iterator(myStack):
            npFrame = np.array(frame,np.uint16)        
            multFrame = np.multiply(npFrame,unoTh)
            medianArray[cntFr]=np.median(multFrame)
            cntFr = cntFr+1
 
#        noiseCoeff = int(np.mean(medianArray))
#        print noiseCoeff
                      
        lineScan = []
        iFrame = 0
               
        for frame in ImageSequence.Iterator(myStack):                

            iFrame = iFrame+1
            
            grayFrame = np.array(frame,np.uint16)
            bgSubFrame = np.clip(grayFrame,int(medianArray[iFrame-1]),None)
            bgSubFrame[bgSubFrame != 0] -= int(medianArray[iFrame-1])
            bgSubFrame = grayFrame
                                  
            if iFrame == 1:
                frW = bgSubFrame.shape[1]
            
            oneFrameScan = np.zeros(frW)

            for k in range(0,frW):
                oneFrameScan[k] = np.sum(bgSubFrame[:,k])
                
            lineScan.append(oneFrameScan)
           
            del oneFrameScan           
            
            
        lineScanMap = np.transpose(np.asarray(lineScan))
        allMax = np.amax(lineScanMap)
        allMin = np.amin(lineScanMap)
        
        scanH = lineScanMap.shape[0]
        scanW = lineScanMap.shape[1]
       
        diffLineScan = np.zeros(shape=(scanH,scanW),dtype=float)
        normLineScan = np.zeros(shape=(scanH,scanW),dtype=float)
        uintLineScan = np.zeros(shape=(scanH,scanW),dtype=float)
       
        for m in range(0,scanH):
            uintLineScan[m,:] = ((lineScanMap[m,:]-allMin)/(allMax-allMin))*65535.
            tempMax = np.amax(lineScanMap[m,:])
            diffLineScan[m,:] = tempMax-lineScanMap[m,:]
                  
        for m in range(0,scanH):
            tempMaxDiff = np.amax(diffLineScan[m,:])
            if tempMaxDiff > 0:
                normLineScan[m,:] = (diffLineScan[m,:]/tempMaxDiff)*65535.
                normLineScan[m,:] = np.clip(normLineScan[m,:],0,65535)
            else:
                normLineScan[m,:] = 0
                
        uint16lineScan = normLineScan.astype('uint16')
        uint16lineScan = np.flipud(uint16lineScan)      
        uint16lineScanInv = cv2.bitwise_not(uint16lineScan) # Inverting Scale - Black=65535
        imlineScanMap = Image.fromarray(uint16lineScanInv)
#                invLineScanMap = PIL.ImageOps.invert(imlineScanMap)
        outFile = directory+'/'+rootStackName+'_STM_LineByLine.tif'
        imlineScanMap.save(outFile,compression = 'None')
        
#        print allMax, np.amin(uintLineScan), np.amax(uintLineScan)
        
        uint16Scan = uintLineScan.astype('uint16')
        uint16Scan = np.flipud(uint16Scan)
#        uint16ScanInv = cv2.bitwise_not(uint16Scan)
        imgLineScan = Image.fromarray(uint16Scan)
        outImg = directory+'/'+rootStackName+'_STM.tif'
        imgLineScan.save(outImg,compression = 'None')
        
        myStack.close()
    
    
          


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fluoWindow = QtWidgets.QMainWindow()
    ui = Ui_fluoWindow()
    ui.setupUi(fluoWindow)
    fluoWindow.show()
    sys.exit(app.exec_())

