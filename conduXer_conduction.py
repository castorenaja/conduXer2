# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer_conduction.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import subprocess
import os.path
from math import factorial
import time


class Ui_conduWindow(object):
    def setupConduUi(self, conduWindow):
        conduWindow.setObjectName("contraWindow")
        conduWindow.resize(941, 561)
        self.centralwidget = QtWidgets.QWidget(conduWindow)
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
        self.inputFileLabel.setGeometry(QtCore.QRect(29, 202, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.inputFileLabel.setFont(font)
        self.inputFileLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputFileLabel.setObjectName("inputFileLabel")
        self.inputFileEntry = QtWidgets.QListWidget(self.centralwidget)
        self.inputFileEntry.setGeometry(QtCore.QRect(130, 190, 641, 41))
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
        self.browseButton.setGeometry(QtCore.QRect(780, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.fpsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsLabel.setGeometry(QtCore.QRect(30, 270, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fpsEntry.setGeometry(QtCore.QRect(200, 260, 61, 41))
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
        self.fpsEntry.setCursorPosition(3)
        self.fpsEntry.setObjectName("fpsEntry")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(720, 450, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/conduction.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.contraAnalysisLabel = QtWidgets.QLabel(self.centralwidget)
        self.contraAnalysisLabel.setGeometry(QtCore.QRect(370, 360, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.contraAnalysisLabel.setFont(font)
        self.contraAnalysisLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.contraAnalysisLabel.setObjectName("contraAnalysisLabel")
        self.contraOpt = QtWidgets.QSlider(self.centralwidget)
        self.contraOpt.setGeometry(QtCore.QRect(600, 350, 71, 41))
        self.contraOpt.setMaximum(1)
        self.contraOpt.setProperty("value", 0)
        self.contraOpt.setSliderPosition(0)
        self.contraOpt.setOrientation(QtCore.Qt.Horizontal)
        self.contraOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.contraOpt.setObjectName("contraOpt")
        self.optYes = QtWidgets.QLabel(self.centralwidget)
        self.optYes.setGeometry(QtCore.QRect(650, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optYes.setFont(font)
        self.optYes.setAlignment(QtCore.Qt.AlignCenter)
        self.optYes.setObjectName("optYes")
        self.optNot = QtWidgets.QLabel(self.centralwidget)
        self.optNot.setGeometry(QtCore.QRect(580, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optNot.setFont(font)
        self.optNot.setAlignment(QtCore.Qt.AlignCenter)
        self.optNot.setObjectName("optNot")
        self.pixCalibLabel = QtWidgets.QLabel(self.centralwidget)
        self.pixCalibLabel.setGeometry(QtCore.QRect(320, 270, 271, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.pixCalibLabel.setFont(font)
        self.pixCalibLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pixCalibLabel.setObjectName("pixCalibLabel")
        self.calibEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.calibEntry.setGeometry(QtCore.QRect(590, 260, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calibEntry.sizePolicy().hasHeightForWidth())
        self.calibEntry.setSizePolicy(sizePolicy)
        self.calibEntry.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.calibEntry.setFont(font)
        self.calibEntry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calibEntry.setCursorPosition(4)
        self.calibEntry.setObjectName("calibEntry")
        self.optYes_2 = QtWidgets.QLabel(self.centralwidget)
        self.optYes_2.setGeometry(QtCore.QRect(290, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optYes_2.setFont(font)
        self.optYes_2.setAlignment(QtCore.Qt.AlignCenter)
        self.optYes_2.setObjectName("optYes_2")
        self.twoPtconduLabel = QtWidgets.QLabel(self.centralwidget)
        self.twoPtconduLabel.setGeometry(QtCore.QRect(30, 360, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.twoPtconduLabel.setFont(font)
        self.twoPtconduLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.twoPtconduLabel.setObjectName("twoPtconduLabel")
        self.optNot_2 = QtWidgets.QLabel(self.centralwidget)
        self.optNot_2.setGeometry(QtCore.QRect(220, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optNot_2.setFont(font)
        self.optNot_2.setAlignment(QtCore.Qt.AlignCenter)
        self.optNot_2.setObjectName("optNot_2")
        self.twoPtOpt = QtWidgets.QSlider(self.centralwidget)
        self.twoPtOpt.setGeometry(QtCore.QRect(240, 350, 71, 41))
        self.twoPtOpt.setMaximum(1)
        self.twoPtOpt.setProperty("value", 0)
        self.twoPtOpt.setSliderPosition(0)
        self.twoPtOpt.setOrientation(QtCore.Qt.Horizontal)
        self.twoPtOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.twoPtOpt.setObjectName("twoPtOpt")
        self.twoPtCondSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.twoPtCondSpeedLabel.setGeometry(QtCore.QRect(30, 490, 321, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.twoPtCondSpeedLabel.setFont(font)
        self.twoPtCondSpeedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.twoPtCondSpeedLabel.setObjectName("twoPtCondSpeedLabel")
        self.condSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.condSpeedLabel.setGeometry(QtCore.QRect(30, 450, 261, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.condSpeedLabel.setFont(font)
        self.condSpeedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.condSpeedLabel.setObjectName("condSpeedLabel")
        self.condSpeedValue = QtWidgets.QLabel(self.centralwidget)
        self.condSpeedValue.setGeometry(QtCore.QRect(360, 450, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.condSpeedValue.setFont(font)
        self.condSpeedValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.condSpeedValue.setObjectName("condSpeedValue")
        self.twoPtCondSpeedValue = QtWidgets.QLabel(self.centralwidget)
        self.twoPtCondSpeedValue.setGeometry(QtCore.QRect(360, 490, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.twoPtCondSpeedValue.setFont(font)
        self.twoPtCondSpeedValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.twoPtCondSpeedValue.setObjectName("twoPtCondSpeedValue")
        self.inputFileLabel.raise_()
        self.inputFileEntry.raise_()
        self.browseButton.raise_()
        self.fpsLabel.raise_()
        self.fpsEntry.raise_()
        self.runButton.raise_()
        self.label.raise_()
        self.titleLabel.raise_()
        self.contraAnalysisLabel.raise_()
        self.contraOpt.raise_()
        self.optYes.raise_()
        self.optNot.raise_()
        self.pixCalibLabel.raise_()
        self.calibEntry.raise_()
        self.optYes_2.raise_()
        self.twoPtconduLabel.raise_()
        self.optNot_2.raise_()
        self.twoPtOpt.raise_()
        self.twoPtCondSpeedLabel.raise_()
        self.condSpeedLabel.raise_()
        self.condSpeedValue.raise_()
        self.twoPtCondSpeedValue.raise_()
        conduWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(conduWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 21))
        self.menubar.setObjectName("menubar")
        conduWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(conduWindow)
        self.statusbar.setObjectName("statusbar")
        conduWindow.setStatusBar(self.statusbar)

        self.retranslateUi(conduWindow)
        QtCore.QMetaObject.connectSlotsByName(conduWindow)

# Added ================       
 
        self.initiateWidgets()

# =====================

    def retranslateUi(self, conduWindow):
        _translate = QtCore.QCoreApplication.translate
        conduWindow.setWindowTitle(_translate("conduWindow", "MainWindow"))
        self.titleLabel.setText(_translate("conduWindow", "conduXer: Conduction Analysis"))
        self.inputFileLabel.setText(_translate("conduWindow", "Input File:"))
        self.browseButton.setText(_translate("conduWindow", "Browse"))
        self.fpsLabel.setText(_translate("conduWindow", "Frame Rate (fps):"))
        self.fpsEntry.setText(_translate("conduWindow", "248"))
        self.runButton.setText(_translate("conduWindow", "RUN"))
        self.contraAnalysisLabel.setText(_translate("conduWindow", "Contraction Analysis:"))
        self.optYes.setText(_translate("conduWindow", "Yes"))
        self.optNot.setText(_translate("conduWindow", "No"))
        self.pixCalibLabel.setText(_translate("conduWindow", "Pixel Calibration (um/pixel):"))
        self.calibEntry.setText(_translate("conduWindow", "1.40"))
        self.optYes_2.setText(_translate("conduWindow", "Yes"))
        self.twoPtconduLabel.setText(_translate("conduWindow", "2-Point Conduction:"))
        self.optNot_2.setText(_translate("conduWindow", "No"))
        self.twoPtCondSpeedLabel.setText(_translate("conduWindow", "2-Point Conduction Speed (mm/s):"))
        self.condSpeedLabel.setText(_translate("conduWindow", "Conduction Speed (mm/s):"))
        self.condSpeedValue.setText(_translate("conduWindow", " "))
        self.twoPtCondSpeedValue.setText(_translate("conduWindow", " "))

 # Added ===========
        
    def initiateWidgets(self):
        self.browseButton.clicked.connect(self.openFileBrowser)
        self.runButton.clicked.connect(self.mainConducFunction)

        
    def openFileBrowser(self):   
        global inFile
        options = QtWidgets.QFileDialog.Options()
#        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select STM File", "", "TIFF Files (*.tif)", options=options)
#        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select STM File", "", "TIFF Files (*.tif *.png)", options=options)
#        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Contraction Video File", "", "Video Files (*.avi)", options=options)
#        if inFile:
#            print(inFile)
        self.inputFileEntry.addItem(inFile)
        del options

    def mainConducFunction(self): 
        
        global inFile, fSp, cid, currCoords, roiCoords, fps, fullSTMap, myScale
        
        fps = int(self.fpsEntry.text())
        contraOption = self.contraOpt.value()
        twoPtCondOption = self.twoPtOpt.value()
        myScale = float(self.calibEntry.text())
               
        fullSTMap = cv2.imread(inFile,0)
        
        fSp = plt.figure(figsize=(16,8))
        ax = fSp.add_subplot(111)
        ax.imshow(fullSTMap,cmap='gray')
        plt.axes().set_aspect(0.2)
            
        currCoords = []
        roiCoords = []

        cid = fSp.canvas.mpl_connect('button_press_event', self.onROIClick)

        plt.show()


    def onROIClick(self,event):
     
        xROICoord, yROICoord = event.xdata, event.ydata

        myROICoords = []

        myROICoords.append((xROICoord,yROICoord))
        roiCoords.append(myROICoords)
       
        if len(roiCoords) == 2:
            fSp.canvas.mpl_disconnect(cid)
            plt.close(fSp)

            firstROICoords = np.transpose(np.asarray(roiCoords[0]))
            secondROICoords = np.transpose(np.asarray(roiCoords[1]))

            global roiUnoCx, roiDosCx

            roiUnoCx = int(firstROICoords[0])
            roiDosCx = int(secondROICoords[0])

            global roiSp, roiCid, STMap, normSTMap, normSTMapUint8, aspectRatio

            normSTMap = fullSTMap[:,roiUnoCx:roiDosCx]
            STMap = cv2.bitwise_not(normSTMap) # Inverting Scale - Black=255

            normSTMapHeight = normSTMap.shape[0]

#            # Normalizing Line-by-Line 0-255
            for i in range(0,normSTMapHeight):
                tmpLineMin = np.amin(normSTMap[i,:])
                tmpLineMax = np.amax(normSTMap[i,:])
                normSTMap[i,:] = ((normSTMap[i,:].astype(float)-tmpLineMin)/(tmpLineMax-tmpLineMin))*255.

            normSTMapUint8 = normSTMap.astype('uint8')


            roiSp = plt.figure(figsize=(16,8))
            axis = roiSp.add_subplot(111)

#            axis.imshow(normSTMapUint8,cmap=plt.cm.gray, vmin=100, vmax=255)
            axis.imshow(normSTMapUint8,cmap=plt.cm.gray)
            
            aspectRatio = float(normSTMapUint8.shape[1])/float(normSTMapUint8.shape[0])
            plt.axes().set_aspect(aspectRatio)

            roiCid = roiSp.canvas.mpl_connect('button_press_event', self.onClick)

        plt.show()
        

    def onClick(self,event):
       
        xCoord, yCoord = event.xdata, event.ydata

        myCoords = []

        global currCoords

        myCoords.append((xCoord,yCoord))
        currCoords.append(myCoords)
       
        if len(currCoords) == 2:
            roiSp.canvas.mpl_disconnect(roiCid)
            plt.close(roiSp)
            self.condAnalysisTool()


## Conduction Analysis Function =================================================
            

    def condAnalysisTool(self):

        oneFrame = 1/float(fps)

        firstCoords = np.transpose(np.asarray(currCoords[0]))
        secondCoords = np.transpose(np.asarray(currCoords[1]))

        unoCx = float(firstCoords[0])
        unoCy = float(firstCoords[1])
        dosCx = float(secondCoords[0])
        dosCy = float(secondCoords[1])

        if (unoCy > dosCy):
            dosCx = float(firstCoords[0])
            dosCy = float(firstCoords[1])

            unoCx = float(secondCoords[0])
            unoCy = float(secondCoords[1])

        if (dosCx != unoCx):
            inSlope = (dosCx-unoCx)/(dosCy-unoCy)
        else:
            inSlope = 0.016

        inOrd = unoCx-(inSlope*unoCy)

        if (inSlope != 0):
            inSpeed = abs(1/inSlope)
            inSpeed = (inSpeed/oneFrame)*myScale*1e-3
            strDosPtSpeed = '{:.2f}'.format(inSpeed)
            _translate = QtCore.QCoreApplication.translate
            self.twoPtCondSpeedValue.setStyleSheet('color: blue')
            self.twoPtCondSpeedValue.setText(_translate("conducWindow", strDosPtSpeed+' mm/s'))
        else:
            strDosPtSpeed = "OOR"
            self.twoPtCondSpeedValue.setStyleSheet('color: blue')
            self.twoPtCondSpeedValue.setText(_translate("conducWindow", strDosPtSpeed+' mm/s'))
            
        strCondSpeed = strDosPtSpeed               

        strErrCondSpeed = ""
        sigmaVar = 0.

#        if self.twoPtCondSpeedValue.value() == 1:
#            modeVar = "2Pt-Cond"

#        if self.checkDist.get():
#            strCondSpeed = ""
#            modeVar = "Distance"

        vLength = STMap.shape[0]*myScale
        strVLength = '{:.2f}'.format(vLength)

        nPixels = STMap.shape[0]
        nFrames = STMap.shape[1]

        yUno = int(unoCy)
        yDos = int(dosCy)

        yDim = abs(yDos-yUno)

        myTime = np.arange(0,nFrames,1)
#        pixelLoc = np.arange(yUno,yDos,1)         

        inLine = np.zeros(yDim,dtype=float)
        fltSTMap = np.zeros(shape=(yDim,nFrames),dtype=float)
        diffSTMap = np.zeros(shape=(yDim,nFrames-1),dtype=float)
        fltDiffSTMap = np.zeros(shape=(yDim,nFrames-1),dtype=float)
#        fltdiffSTMap = np.zeros(shape=(yDim,nFrames-1),dtype=float)
#        maxDiff = np.zeros(yDim,dtype=float)
        locPix = np.zeros(yDim,dtype=int)
        loc = np.arange(0,yDim,dtype=int)

        winSize = int(np.rint(4*0.02*fps))
        
        condSTM = normSTMapUint8[yUno:yDos,:]

        for i in range(0,yDim):
            try:
                del tmpInf, tmpSup
            except:
                pass
            inLine[i] = (inSlope*(i+yUno))+inOrd
            tmpInf = int(inLine[i]*0.80)
            tmpSup = int(inLine[i]*1.20)
            fltSTMap[i,:] = self.savitzky_golay(condSTM[i,:], 91, 5)
            tmpLineMax = np.amax(fltSTMap[i,tmpInf:tmpSup])
            diffSTMap[i,:] = np.diff(fltSTMap[i,:])
            fltDiffSTMap[i,:] = self.savitzky_golay(diffSTMap[i,:], 91, 5)
            
            tmpDiff = -1.
            runIndex = tmpSup
            if diffSTMap[i,runIndex] < 0.:
                while (tmpDiff < 0.):
                    tmpDiff = diffSTMap[i,runIndex]
                    runIndex = runIndex-1
                runIndex = runIndex-2 #Correction for pixel lost during differentiation plus one 
            else:
                runIndex = 0

            
            locPix[i] = runIndex
            
        fitPar, cov = np.polyfit(loc,locPix,1,cov=True)
        slope = fitPar[0]

        fitLine = np.zeros(yDim,dtype=float)

        for i in range(0,yDim):
            fitLine[i] = (slope*(1+i))+fitPar[1]

        for i in range(0,yDim):
            tmpDist = abs(fitLine[i]-locPix[i])
            if tmpDist > winSize:
                locPix[i] = 0
            else:
                pass
            
        selLocPix = locPix[np.nonzero(locPix)]
        selLocs = loc[np.nonzero(locPix)]
        
        try:
            del fitPar, cov, slope
        except:
            pass
        
        fitPar, cov = np.polyfit(selLocs,selLocPix,1,cov=True)
        slope = fitPar[0]

        selDim = selLocPix.shape[0]

        selfitLine = np.zeros(yDim,dtype=float)

        for i in range(0,yDim):
            selfitLine[i] = (slope*(1+i))+fitPar[1]

        if (slope != 0):
            speed = abs(1/slope)
            speed = (speed/oneFrame)*myScale*1e-3
            strSpeed = '{:.2f}'.format(speed)
            _translate = QtCore.QCoreApplication.translate
            self.condSpeedValue.setStyleSheet('color: blue')
            self.condSpeedValue.setText(_translate("conducWindow", strSpeed+' mm/s'))
        else:
            strSpeed = "OOR"
            self.condSpeedValue.setStyleSheet('color: blue')
            self.condSpeedValue.setText(_translate("conducWindow", strSpeed+' mm/s'))
            

            
                
#            tmpIndx = np.argmax(diffSTMap[i,np.argmax(fltSTMap[i,:]):np.argmin(fltSTMap[i,:])])
#            tmpIndx = tmpIndx+np.argmax(fltSTMap[i,:])
#            locPix[i]=tmpIndx
#            zeroCnt = 0
#            for n in range(0,tmpIndx):
#                if diffSTMap[i,tmpIndx-n] < 0:
#                    zeroCnt = zeroCnt+1
#            locPix[i]=tmpIndx-zeroCnt
#            maxDiff[i] = np.argmax(diffSTMap[i])
#            locDev = abs(maxDiff[i]-inLine[i])
#            if locDev > winSize:
#                maxDiff[i] = 0
#            else:
#                pass         
            
#        fUno = plt.figure(figsize=(14,8))
#        ax = fUno.add_subplot(111)                   
#        ax.tick_params(axis='both', direction='inout', length=8, width=3) 
##        shiftTime = Time-minTime
#        h = condSTM.shape[0]
#        w = condSTM.shape[1]
##        plt.plot(np.arange(0,w-1),diffSTMap[int(h/2),:],'k-')
##        plt.plot(np.arange(0,w-1),fltDiffSTMap[int(h/2),:],'k-')
#        plt.plot(np.arange(0,w-1),fltSTMap[int(h/2),:-1],'rs')
#        plt.plot(np.arange(0,w-1),fltSTMap[int(h/3),:-1],'r-')
#        plt.plot(np.arange(0,w-1),fltSTMap[int(h/4),:-1],'r-')
#        plt.plot(np.arange(0,w-1),fltSTMap[int(h/5),:-1],'r-')
#        myXlabel = ax.set_xlabel('Time (seconds)')
#        EmLabel = 'E$_\mathrm{m}$'
#        plt.ylabel(EmLabel+'(mV)')
#        plt.xlim((0,maxTime-minTime))  
#        plt.ylim((-50,0))
            
#        if (self.checkCa.get() or self.checkCaLS.get()):
#            modeVar = "Ca2+"
#        if self.checkContra.get():
#            modeVar = "Contraction"

# ====
          
#        dataPoints = maxDiff[np.nonzero(maxDiff)]
#        locPixels = pixelLoc[np.nonzero(maxDiff)]
#
#        pixelCount = (float(len(dataPoints))/yDim)*100
#
#        roiLocPixels = []
#        roiDataPoints = []
#
#        roiLocPixels = locPixels[np.where(np.logical_and(locPixels>=unoCy, locPixels<=dosCy))]       
#        roiDataPoints = dataPoints[np.where(np.logical_and(locPixels>=unoCy, locPixels<=dosCy))]
# 
#        fitPar, cov = np.polyfit(roiLocPixels,roiDataPoints,1,cov=True)
#        slope = fitPar[0]
#        slopeSigma = np.sqrt(np.diag(cov))[0]
#
#        fitLine = np.zeros(yDim,dtype=float)
#
#        for i in range(yUno,yDos):
#            fitLine[i-yUno] = (slope*(1+i))+fitPar[1]
#        
#        condSpeed = abs(1/slope)
#        condSpeed = (condSpeed/oneFrame)*myScale*1e-3
#        errCondSpeed = abs(slopeSigma/(slope*slope))
#
##        strErrCondSpeed = '{:.2f}'.format(errCondSpeed)
###            self.errCxSpeed.set(strErrCondSpeed + '  mm/s')
#        
#        strCondSpeed = '{:.2f}'.format(condSpeed)
#        self.condSpeedValue.setStyleSheet('color: blue')
#        self.condSpeedValue.setText(_translate("conducWindow", strCondSpeed+' mm/s'))
#        
##        sigmaVar = pixelCount
##
##        if pixelCount >= 50.:
##            strSigmaVar = '{:.2f}'.format(sigmaVar)+'%'
##        if pixelCount < 50:
##            strSigmaVar = '{:.2f}'.format(sigmaVar)+'%'+'  (Warning!)'
##
##        self.sigmaTest.set(strSigmaVar)
##        strSigmaVar = '{:.2f}'.format(sigmaVar)
#
#        fSp = plt.figure(figsize=(16,8))
#        ax = fSp.add_subplot(111)
#        imData = ax.imshow(normSTMapUint8,cmap=plt.cm.gray, vmin=0, vmax=255)
#        plt.plot(roiDataPoints,roiLocPixels,'rs',markersize=4)
#        plt.plot(fitLine,pixelLoc,'-y')
#        plt.axes().set_aspect(0.04)

        yPos = np.arange(0,yDim)
        fSp = plt.figure(figsize=(16,8))
        ax = fSp.add_subplot(111)
        imData = ax.imshow(condSTM,cmap=plt.cm.gray, vmin=0, vmax=255)
#        plt.plot(locPix,yPos,'rs',markersize=4)
        plt.plot(inLine,yPos,'ys',markersize=2)
        plt.plot(selLocPix,selLocs,'gs',markersize=4)
#        plt.plot(locPix,yPos,'rs',markersize=4)
        plt.plot(selfitLine,loc,'b-')
        plt.axes().set_aspect(aspectRatio)

#        myTime = time.strftime("%H:%M")
#        myDate = time.strftime("%m/%d/%Y")
#
#        desktopPath = os.path.expanduser('~') + '/Desktop/'
#        cxDirectory = desktopPath + "conduXer"
#
#        fileName = cxDirectory + "/conduXerData.xlsx" 
#        dataFile = fileName
#
#        imgName = inFile.split("/")[-1]
#        directory = inFile[:-len(imgName)]+'/'+imgName[:-4]
#        rootVideoName = imgName[:-4]
#        
#        if not os.path.exists(directory):
#            os.makedirs(directory)

#        distLength = ((dosCy-unoCy)*myScale)
#        percentCL = ((dosCy-unoCy)/nPixels)*100.
#
#        if self.checkFullCond.get():
#            distLength = nPixels*myScale
#            percentCL = 100.            
#        
#        percentCL = '{:.2f}'.format(percentCL)
#        self.percentCondDist.set(percentCL)
#        strDistLength = '{:.2f}'.format(distLength)
#        self.condDist.set( strDistLength + ' um')
#        roiString =  '{:.2f}'.format(oneFrame*roiUnoCx) + "(" + '{:.2f}'.format(roiUnoCx) + ")"  +" - "+  '{:.2f}'.format(oneFrame*roiDosCx) + "(" + '{:.2f}'.format(roiDosCx) + ")"
#
#        strFileName = inFile.split("/")[-1]
#
#        conduXerVer = 'v9'
#
#        myHeader = ['Date','Time','Obj','FPS','Mode','FileName','CondSpeed','ErrCondSpeed','DataPointsUsed','ConductionLength','PercentCondLength','VesselLength','timeROI','Version']
#        myUnits = {'Date':'MM/DD/YY','Time':'HH:MM:SS','Obj':'(um/pixel)','FPS':'','Mode':'','FileName':' ','CondSpeed':'mm/s','ErrCondSpeed':'mm/s','DataPointsUsed':'(%)','ConductionLength':'um','PercentCondLength':'(%)','VesselLength':'um','timeROI':'seconds(frames)','Version':''}
#
#        if self.check2PtCond.get():
#            if (inSlope != 0):
#                data = {'Date':time.strftime("%m/%d/%Y"),'Time':time.strftime("%H:%M:%S"),'Obj':objVar,'FPS':myFPS,'Mode':modeVar,'FileName':strFileName,'CondSpeed':float(strCondSpeed),'ErrCondSpeed':'-','DataPointsUsed':'-','ConductionLength':float(strDistLength),'PercentCondLength':float(percentCL),'VesselLength':float(strVLength),'timeROI':roiString,'Version':conduXerVer}
#            else:
#                data = {'Date':time.strftime("%m/%d/%Y"),'Time':time.strftime("%H:%M:%S"),'Obj':objVar,'FPS':myFPS,'Mode':modeVar,'FileName':strFileName,'CondSpeed':'-','ErrCondSpeed':'-','DataPointsUsed':'-','ConductionLength':float(strDistLength),'PercentCondLength':float(percentCL),'VesselLength':float(strVLength),'timeROI':roiString,'Version':conduXerVer}
#        else:
#            data = {'Date':time.strftime("%m/%d/%Y"),'Time':time.strftime("%H:%M:%S"),'Obj':objVar,'FPS':myFPS,'Mode':modeVar,'FileName':strFileName,'CondSpeed':float(strCondSpeed),'ErrCondSpeed':float(strErrCondSpeed),'DataPointsUsed':float(strSigmaVar),'ConductionLength':float(strDistLength),'PercentCondLength':float(percentCL),'VesselLength':float(strVLength),'timeROI':roiString,'Version':conduXerVer}
#
#        if ( not os.path.isfile(dataFile)):         
#
#            myDF = pandas.DataFrame(columns=myHeader)
#            myuDF = myDF.append(myUnits, ignore_index=True)
#            myDFF = myuDF.append(data, ignore_index=True)
#            myWriter = pandas.ExcelWriter(dataFile, engine='xlsxwriter')
#            myDFF.to_excel(myWriter,index=False,sheet_name='Records')
#            myWorkbook = myWriter.book
#            myWorksheet = myWriter.sheets['Records']
#            myWorksheet.set_zoom(90)
#            myWorksheet.set_column('A:B',12)
#            myWorksheet.set_column('C:C',16)
#            myWorksheet.set_column('D:D',6)
#            myWorksheet.set_column('E:E',12)
#            myWorksheet.set_column('F:F',70)
#            myWorksheet.set_column('G:L',17)
#            myWorksheet.set_column('M:M',35)
#            myWorksheet.set_column('N:N',12)
#            myWorkbook.add_format({'align':'center','valign':'vcenter'})
#            myWriter.save()
#        else:
#            myCurrentDF = pandas.read_excel(dataFile,sheet_name='Records')
#            myAppendDF = myCurrentDF.append(data, ignore_index=True)
#            myWriter = pandas.ExcelWriter(dataFile, engine='xlsxwriter')
#            myAppendDF.to_excel(myWriter,index=False,sheet_name='Records')
#            myWorkbook = myWriter.book
#            myWorksheet = myWriter.sheets['Records']
#            myWorksheet.set_zoom(90)
#            myWorksheet.set_column('A:B',12)
#            myWorksheet.set_column('C:C',16)
#            myWorksheet.set_column('D:D',6)
#            myWorksheet.set_column('E:E',12)
#            myWorksheet.set_column('F:F',70)
#            myWorksheet.set_column('G:L',17)
#            myWorksheet.set_column('M:M',35)
#            myWorksheet.set_column('N:N',12)
#            myWorkbook.add_format({'align':'center','valign':'vcenter'})
#            myWriter.save()

#        if (self.checkCa.get() or self.checkCaLS.get() or self.checkContra.get()):       
        plt.show()
#
#        subprocess.call("cls", shell=True)
#        tempStr = "Done!"
#        subprocess.call(["echo", tempStr], shell=True)

    def savitzky_golay(self, y, window_size, order, deriv=0, rate=1):
        r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
        The Savitzky-Golay filter removes high frequency noise from data.
        It has the advantage of preserving the original shape and
        features of the signal better than other types of filtering
        approaches, such as moving averages techniques.
        Parameters
        ----------
        y : array_like, shape (N,)
            the values of the time history of the signal.
        window_size : int
            the length of the window. Must be an odd integer number.
        order : int
            the order of the polynomial used in the filtering.
            Must be less then `window_size` - 1.
        deriv: int
            the order of the derivative to compute (default = 0 means only smoothing)
        Returns
        -------
        ys : ndarray, shape (N)
            the smoothed signal (or it's n-th derivative).
        Notes
        -----
        The Savitzky-Golay is a type of low-pass filter, particularly
        suited for smoothing noisy data. The main idea behind this
        approach is to make for each point a least-square fit with a
        polynomial of high order over a odd-sized window centered at
        the point.
        Examples
        --------
        t = np.linspace(-4, 4, 500)
        y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
        ysg = savitzky_golay(y, window_size=31, order=4)
        import matplotlib.pyplot as plt
        plt.plot(t, y, label='Noisy signal')
        plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
        plt.plot(t, ysg, 'r', label='Filtered signal')
        plt.legend()
        plt.show()
        References
        ----------
        .. [1] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of
           Data by Simplified Least Squares Procedures. Analytical
           Chemistry, 1964, 36 (8), pp 1627-1639.
        .. [2] Numerical Recipes 3rd Edition: The Art of Scientific Computing
           W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
           Cambridge University Press ISBN-13: 9780521880688
        """
        
        try:
            window_size = np.abs(np.int(window_size))
            order = np.abs(np.int(order))
        except ValueError, msg:
            raise ValueError("window_size and order have to be of type int")
        if window_size % 2 != 1 or window_size < 1:
            raise TypeError("window_size size must be a positive odd number")
        if window_size < order + 2:
            raise TypeError("window_size is too small for the polynomials order")
        order_range = range(order+1)
        half_window = (window_size -1) // 2
        # precompute coefficients
        b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
        m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
        # pad the signal at the extremes with
        # values taken from the signal itself
        firstvals = y[0] - np.abs(y[1:half_window+1][::-1] - y[0])
        lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
        y = np.concatenate((firstvals, y, lastvals))
        return np.convolve( m[::-1], y, mode='valid')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conduWindow = QtWidgets.QMainWindow()
    ui = Ui_conduWindow()
    ui.setupConduUi(conduWindow)
    conduWindow.show()
    sys.exit(app.exec_())

