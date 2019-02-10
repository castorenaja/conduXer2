# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer_nirf.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
import numpy as np
from matplotlib import pyplot as plt
import subprocess
import matplotlib.patches as patches
from math import factorial


class Ui_nirfWindow(object):
    def setupNirfUi(self, nirfWindow):
        nirfWindow.setObjectName("nirfWindow")
        nirfWindow.resize(920, 574)
        self.centralwidget = QtWidgets.QWidget(nirfWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 20, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(25)
        self.titleLabel.setFont(font)
        self.titleLabel.setAutoFillBackground(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.inputFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputFileLabel.setGeometry(QtCore.QRect(29, 212, 151, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.inputFileLabel.setFont(font)
        self.inputFileLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputFileLabel.setObjectName("inputFileLabel")
        self.inputFileEntry = QtWidgets.QListWidget(self.centralwidget)
        self.inputFileEntry.setGeometry(QtCore.QRect(130, 200, 641, 41))
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
        self.browseButton.setGeometry(QtCore.QRect(780, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.fpsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsLabel.setGeometry(QtCore.QRect(30, 300, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fpsEntry.setGeometry(QtCore.QRect(200, 290, 41, 41))
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
        self.fpsEntry.setCursorPosition(1)
        self.fpsEntry.setObjectName("fpsEntry")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(710, 460, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 921, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/nirf.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.calibLabel = QtWidgets.QLabel(self.centralwidget)
        self.calibLabel.setGeometry(QtCore.QRect(280, 300, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.calibLabel.setFont(font)
        self.calibLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.calibLabel.setObjectName("calibLabel")
        self.displayFramesOpt = QtWidgets.QSlider(self.centralwidget)
        self.displayFramesOpt.setGeometry(QtCore.QRect(810, 290, 71, 41))
        self.displayFramesOpt.setMaximum(1)
        self.displayFramesOpt.setSliderPosition(0)
        self.displayFramesOpt.setOrientation(QtCore.Qt.Horizontal)
        self.displayFramesOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.displayFramesOpt.setObjectName("displayFramesOpt")
        self.dispOptNot = QtWidgets.QLabel(self.centralwidget)
        self.dispOptNot.setGeometry(QtCore.QRect(790, 260, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptNot.setFont(font)
        self.dispOptNot.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptNot.setObjectName("dispOptNot")
        self.dispOptYes = QtWidgets.QLabel(self.centralwidget)
        self.dispOptYes.setGeometry(QtCore.QRect(860, 260, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptYes.setFont(font)
        self.dispOptYes.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptYes.setObjectName("dispOptYes")
        self.displayFramesLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayFramesLabel.setGeometry(QtCore.QRect(620, 300, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.displayFramesLabel.setFont(font)
        self.displayFramesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.displayFramesLabel.setObjectName("displayFramesLabel")
        self.calibEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.calibEntry.setGeometry(QtCore.QRect(500, 290, 71, 41))
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
        self.calibEntry.setCursorPosition(5)
        self.calibEntry.setObjectName("calibEntry")
        self.filterLabel = QtWidgets.QLabel(self.centralwidget)
        self.filterLabel.setGeometry(QtCore.QRect(390, 390, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.filterLabel.setFont(font)
        self.filterLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filterLabel.setObjectName("filterLabel")
        self.filterSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.filterSpinBox.setGeometry(QtCore.QRect(550, 380, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setKerning(True)
        self.filterSpinBox.setFont(font)
        self.filterSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.filterSpinBox.setMaximum(7)
        self.filterSpinBox.setProperty("value", 3)
        self.filterSpinBox.setObjectName("filterSpinBox")
        self.filterLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.filterLabel_2.setGeometry(QtCore.QRect(650, 380, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.filterLabel_2.setFont(font)
        self.filterLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filterLabel_2.setObjectName("filterLabel_2")
        self.filterLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.filterLabel_3.setGeometry(QtCore.QRect(650, 400, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.filterLabel_3.setFont(font)
        self.filterLabel_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filterLabel_3.setObjectName("filterLabel_3")
        self.windowLabel = QtWidgets.QLabel(self.centralwidget)
        self.windowLabel.setGeometry(QtCore.QRect(30, 390, 201, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.windowLabel.setFont(font)
        self.windowLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.windowLabel.setObjectName("windowLabel")
        self.winH = QtWidgets.QLineEdit(self.centralwidget)
        self.winH.setGeometry(QtCore.QRect(240, 380, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winH.sizePolicy().hasHeightForWidth())
        self.winH.setSizePolicy(sizePolicy)
        self.winH.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.winH.setFont(font)
        self.winH.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.winH.setCursorPosition(2)
        self.winH.setObjectName("winH")
        self.winW = QtWidgets.QLineEdit(self.centralwidget)
        self.winW.setGeometry(QtCore.QRect(300, 380, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winW.sizePolicy().hasHeightForWidth())
        self.winW.setSizePolicy(sizePolicy)
        self.winW.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.winW.setFont(font)
        self.winW.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.winW.setCursorPosition(2)
        self.winW.setObjectName("winW")
        self.hLabel = QtWidgets.QLabel(self.centralwidget)
        self.hLabel.setGeometry(QtCore.QRect(240, 350, 51, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.hLabel.setFont(font)
        self.hLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.hLabel.setObjectName("hLabel")
        self.wLabel = QtWidgets.QLabel(self.centralwidget)
        self.wLabel.setGeometry(QtCore.QRect(300, 350, 51, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        self.wLabel.setFont(font)
        self.wLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.wLabel.setObjectName("wLabel")
        self.inputFileLabel.raise_()
        self.inputFileEntry.raise_()
        self.browseButton.raise_()
        self.fpsLabel.raise_()
        self.fpsEntry.raise_()
        self.runButton.raise_()
        self.label.raise_()
        self.titleLabel.raise_()
        self.calibLabel.raise_()
        self.displayFramesOpt.raise_()
        self.dispOptNot.raise_()
        self.dispOptYes.raise_()
        self.displayFramesLabel.raise_()
        self.calibEntry.raise_()
        self.filterLabel.raise_()
        self.filterSpinBox.raise_()
        self.filterLabel_2.raise_()
        self.filterLabel_3.raise_()
        self.windowLabel.raise_()
        self.winH.raise_()
        self.winW.raise_()
        self.hLabel.raise_()
        self.wLabel.raise_()
        nirfWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(nirfWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        nirfWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(nirfWindow)
        self.statusbar.setObjectName("statusbar")
        nirfWindow.setStatusBar(self.statusbar)

        self.retranslateUi(nirfWindow)
        QtCore.QMetaObject.connectSlotsByName(nirfWindow)
        
        # Added ================       
 
        self.initiateWidgets()

        # =====================

    def retranslateUi(self, nirfWindow):
        _translate = QtCore.QCoreApplication.translate
        nirfWindow.setWindowTitle(_translate("nirfWindow", "MainWindow"))
        self.titleLabel.setText(_translate("nirfWindow", "conduXer2: In-Vivo NIRF Analysis"))
        self.inputFileLabel.setText(_translate("nirfWindow", "Input File:"))
        self.browseButton.setText(_translate("nirfWindow", "Browse"))
        self.fpsLabel.setText(_translate("nirfWindow", "Frame Rate (fps):"))
        self.fpsEntry.setText(_translate("nirfWindow", "1"))
        self.runButton.setText(_translate("nirfWindow", "RUN"))
        self.calibLabel.setText(_translate("nirfWindow", "Calibration (um/pixel):"))
        self.dispOptNot.setText(_translate("nirfWindow", "No"))
        self.dispOptYes.setText(_translate("nirfWindow", "Yes"))
        self.displayFramesLabel.setText(_translate("nirfWindow", "Display Frames?"))
        self.calibEntry.setText(_translate("nirfWindow", "18.52"))
        self.filterLabel.setText(_translate("nirfWindow", "Filtering Level:"))
        self.filterLabel_2.setText(_translate("nirfWindow", "0=No Filter"))
        self.filterLabel_3.setText(_translate("nirfWindow", "7=Maximum Filtering"))
        self.windowLabel.setText(_translate("nirfWindow", "Window Size (pixels):"))
        self.winH.setText(_translate("nirfWindow", "20"))
        self.winW.setText(_translate("nirfWindow", "20"))
        self.hLabel.setText(_translate("nirfWindow", "Height"))
        self.wLabel.setText(_translate("nirfWindow", "Width"))

 # Added ===========
        
    def initiateWidgets(self):
        self.browseButton.clicked.connect(self.openFileBrowser)
        self.runButton.clicked.connect(self.inVivoNirfFunction)
     
    def openFileBrowser(self):   
        global inFile
        options = QtWidgets.QFileDialog.Options()
#        options |= QtWidgets.QFileDialog.DontUseNativeDialog
#        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select STM File", "", "TIFF Files (*.tif *.png)", options=options)
        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select NIRF Video File", "", "AVI Files (*.avi)", options=options)
        if inFile:
            print "AVI Successfully Loaded"
        self.inputFileEntry.addItem(inFile)
        del options

    def inVivoNirfFunction(self):
        
        global fps, displayOption, cid, roiCoords, fSp, wH, wW, fltOpt
        
        fps = int(self.fpsEntry.text())
        displayOption = self.displayFramesOpt.value()
        wH = int(self.winH.text())
        wW = int(self.winW.text())
        fltOpt = int(self.filterSpinBox.value())

        
        maxProj = self.maxProjection(inFile)
        
        fSp = plt.figure(figsize=(16,8))
        ax = fSp.add_subplot(111)
        ax.imshow(maxProj,cmap='gray')
        
        roiCoords = []

        cid = fSp.canvas.mpl_connect('button_press_event', self.selectROIs)

        plt.show()        
        
    def selectROIs(self,event):
       
        global firstROICoords, secondROICoords
        
        xROICoord, yROICoord = event.xdata, event.ydata

        myROICoords = []

        myROICoords.append((xROICoord,yROICoord))
        roiCoords.append(myROICoords)
      
        if len(roiCoords) == 2:
            fSp.canvas.mpl_disconnect(cid)
            plt.close(fSp)

            firstROICoords = np.transpose(np.asarray(roiCoords[0]))
            secondROICoords = np.transpose(np.asarray(roiCoords[1]))
                           
            self.nirfVideoReader(inFile, fps)         
     

    def maxProjection(self, inVideo):
        
        try:
            cap = cv2.VideoCapture(inVideo)
        except:
            print 'Error Loading Video File'

        ret, singleFrame = cap.read()
        cap.release()

        frameSize = singleFrame.shape # [height, width]

        frH = frameSize[0]
        frW = frameSize[1]

        cap = cv2.VideoCapture(inVideo)

        sumFrames = np.zeros(shape=(frH,frW),dtype=float)

        while(cap.isOpened()):
            ret, fullFrame = cap.read()
            if(ret==True):
                grayFrame = cv2.cvtColor(fullFrame, cv2.COLOR_BGR2GRAY) # Converting to GrayScale
                sumFrames = cv2.add(sumFrames,np.asanyarray(grayFrame,dtype=np.float))             
                                    
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
            else:
                cap.release()
                cv2.destroyWindow('videoFrames')
                cv2.waitKey(1)
                
        global uint8SumFrame
                
        uint8SumFrame = ((sumFrames/np.amax(sumFrames))*255).astype('uint8')
        
        return uint8SumFrame
        

    def nirfVideoReader(self, inVideo, fps):
        
        try:
            cap = cv2.VideoCapture(inVideo)
        except:
            print 'Error Loading Video File'

        ret, singleFrame = cap.read()
        totalFrames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
        cap.release()

        frameSize = singleFrame.shape # [height, width]

        frH = frameSize[0]
        frW = frameSize[1]

        if displayOption == 1:
            dispFig, dispAx = plt.subplots(1)
            dispFig.set_size_inches(10,7)
            dispFig.canvas.set_window_title("Displaying Video Frames")
                        
        cap = cv2.VideoCapture(inVideo)

        counter = 0

        sumFrames = np.zeros(shape=(frH,frW),dtype=float)
               
        sq1EdgeX = int(firstROICoords[0])-int(wW/2)
        sq1EdgeY = int(firstROICoords[1])-int(wH/2)
        sq2EdgeX = int(secondROICoords[0])-int(wW/2)
        sq2EdgeY = int(secondROICoords[1])-int(wH/2)
        
        roi1sum = np.zeros(totalFrames,dtype=float)
        roi2sum = np.zeros(totalFrames,dtype=float)

        while(cap.isOpened()):
            ret, fullFrame = cap.read()
            if(ret==True):
                grayFrame = cv2.cvtColor(fullFrame, cv2.COLOR_BGR2GRAY) # Converting to GrayScale
                sumFrames = cv2.add(sumFrames,np.asanyarray(grayFrame,dtype=np.float))    
                
                roi1sum[counter] = np.sum(fullFrame[sq1EdgeY:sq1EdgeY+wH,sq1EdgeX:sq1EdgeX+wW])
                roi2sum[counter] = np.sum(fullFrame[sq2EdgeY:sq2EdgeY+wH,sq2EdgeX:sq2EdgeX+wW])

                if displayOption == 1:
                    if counter == 0:
                        dispImg = dispAx.imshow(fullFrame,'gray')
                    
                    if counter > 0:
                        dispImg.set_data(fullFrame)
                        dispFig.canvas.draw()
                        dispFig.canvas.flush_events()
                        
                    sq1 = patches.Rectangle((sq1EdgeX,sq1EdgeY),wW,wH,linewidth=1,edgecolor='b',facecolor='none')                        
                    dispAx.add_patch(sq1)
                    sq2 = patches.Rectangle((sq2EdgeX,sq2EdgeY),wW,wH,linewidth=1,edgecolor='r',facecolor='none')                        
                    dispAx.add_patch(sq2)
                    
                    plt.show()

                    counter = counter + 1
                    
                    if counter == 1:
                        subprocess.call("cls", shell=True)
                        tempStr = "Running..."
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.1):
                        subprocess.call("cls", shell=True)
                        tempStr = "10%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.2):
                        subprocess.call("cls", shell=True)
                        tempStr = "20%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.3):
                        subprocess.call("cls", shell=True)
                        tempStr = "30%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.4):
                        subprocess.call("cls", shell=True)
                        tempStr = "40%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.5):
                        subprocess.call("cls", shell=True)
                        tempStr = "50%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.6):
                        subprocess.call("cls", shell=True)
                        tempStr = "60%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.7):
                        subprocess.call("cls", shell=True)
                        tempStr = "70%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.8):
                        subprocess.call("cls", shell=True)
                        tempStr = "80%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames*0.9):
                        subprocess.call("cls", shell=True)
                        tempStr = "90%_Completed"
                        subprocess.call(["echo", tempStr], shell=True)
                    if counter == int(totalFrames):
                        subprocess.call("cls", shell=True)
                        tempStr = "Video Processing Completed!"
                        subprocess.call(["echo", tempStr], shell=True)
                                    
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
            else:
                cap.release()
                cv2.destroyWindow('videoFrames')
                cv2.waitKey(1)
                
        if fltOpt == 0:
            fltRoi1 = roi1sum
            fltRoi2 = roi2sum
        else:
            if fltOpt == 1:
                fltWin = 7
            if fltOpt == 2:
                fltWin = 11
            if fltOpt == 3:
                fltWin = 21
            if fltOpt == 4:
                fltWin = 31
            if fltOpt == 5:
                fltWin = 51
            if fltOpt == 6:
                fltWin = 71
            if fltOpt == 7:
                fltWin = 151
                
            fltRoi1 = self.savitzky_golay(roi1sum,31,5)
            fltRoi2 = self.savitzky_golay(roi2sum,31,5)

        roi1max = np.amax(fltRoi1)
        roi1min = np.amin(fltRoi1)
        roi2max = np.amax(fltRoi2)
        roi2min = np.amin(fltRoi2)
                      
        nfltRoi1 = (fltRoi1-roi1min)/(roi1max-roi1min)
        nfltRoi2 = (fltRoi2-roi2min)/(roi2max-roi2min)
        
        diffTm = abs(np.argmax(nfltRoi1)-np.argmax(nfltRoi2))
        print diffTm
        
#        dRoi1 = np.diff(nfltRoi1)
#        dRoi2 = np.diff(nfltRoi2)
        
        tbins = np.arange(totalFrames)
        fDos = plt.figure(figsize=(16,8),frameon=False)       
        plt.plot(tbins,nfltRoi1,'b',tbins,nfltRoi2,'r')


#        dtbins = np.arange(totalFrames-1)
#        plt.plot(dtbins,dRoi1,'b',dtbins,dRoi2,'r')
#        plt.plot(tbins,roi1sum,'b',tbins,roi2sum,'r--')
#        plt.xlabel('Frequency (Contractions/Minute)')
#        fDos.savefig(directory+'/'+rootVideoName+'_SFMhisto_conduXer2.png', bbox_inches='tight', pad_inches=0)
#        ##plt.xlim((1,100))
#        ##plt.ylim((0,1e10))
        plt.show()

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
    nirfWindow = QtWidgets.QMainWindow()
    ui = Ui_nirfWindow()
    ui.setupUi(nirfWindow)
    nirfWindow.show()
    sys.exit(app.exec_())

