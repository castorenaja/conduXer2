# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer_contraFourier.ui'
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


class Ui_contraWindow(object):
    def setupContraUi(self, contraWindow):
        contraWindow.setObjectName("contraWindow")
        contraWindow.resize(941, 530)
        contraWindow.setFixedSize(941, 530)
        self.centralwidget = QtWidgets.QWidget(contraWindow)
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
        self.fpsEntry.setGeometry(QtCore.QRect(200, 260, 141, 41))
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
        self.runButton.setGeometry(QtCore.QRect(720, 410, 191, 71))
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
        self.label.setPixmap(QtGui.QPixmap("images/161208_SmmhcCreERT2_Cx45fxfx"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.fourierLabel = QtWidgets.QLabel(self.centralwidget)
        self.fourierLabel.setGeometry(QtCore.QRect(30, 360, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.fourierLabel.setFont(font)
        self.fourierLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fourierLabel.setObjectName("fourierLabel")
        self.resampleSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.resampleSpinBox.setGeometry(QtCore.QRect(580, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.resampleSpinBox.setFont(font)
        self.resampleSpinBox.setMinimum(1)
        self.resampleSpinBox.setMaximum(25)
        self.resampleSpinBox.setObjectName("resampleSpinBox")
        self.resampleLabel = QtWidgets.QLabel(self.centralwidget)
        self.resampleLabel.setGeometry(QtCore.QRect(380, 270, 201, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.resampleLabel.setFont(font)
        self.resampleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.resampleLabel.setObjectName("resampleLabel")
        self.fourierOpt = QtWidgets.QSlider(self.centralwidget)
        self.fourierOpt.setGeometry(QtCore.QRect(220, 350, 71, 41))
        self.fourierOpt.setMaximum(1)
        self.fourierOpt.setSliderPosition(0)
        self.fourierOpt.setOrientation(QtCore.Qt.Horizontal)
        self.fourierOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.fourierOpt.setObjectName("fourierOpt")
        self.optYes = QtWidgets.QLabel(self.centralwidget)
        self.optYes.setGeometry(QtCore.QRect(270, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optYes.setFont(font)
        self.optYes.setAlignment(QtCore.Qt.AlignCenter)
        self.optYes.setObjectName("optYes")
        self.optNot = QtWidgets.QLabel(self.centralwidget)
        self.optNot.setGeometry(QtCore.QRect(200, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optNot.setFont(font)
        self.optNot.setAlignment(QtCore.Qt.AlignCenter)
        self.optNot.setObjectName("optNot")
        self.displayFramesOpt = QtWidgets.QSlider(self.centralwidget)
        self.displayFramesOpt.setGeometry(QtCore.QRect(570, 350, 71, 41))
        self.displayFramesOpt.setMaximum(1)
        self.displayFramesOpt.setSliderPosition(0)
        self.displayFramesOpt.setOrientation(QtCore.Qt.Horizontal)
        self.displayFramesOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.displayFramesOpt.setObjectName("displayFramesOpt")
        self.dispOptNot = QtWidgets.QLabel(self.centralwidget)
        self.dispOptNot.setGeometry(QtCore.QRect(550, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptNot.setFont(font)
        self.dispOptNot.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptNot.setObjectName("dispOptNot")
        self.dispOptYes = QtWidgets.QLabel(self.centralwidget)
        self.dispOptYes.setGeometry(QtCore.QRect(620, 320, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptYes.setFont(font)
        self.dispOptYes.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptYes.setObjectName("dispOptYes")
        self.displayFramesLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayFramesLabel.setGeometry(QtCore.QRect(380, 360, 181, 25))
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
        self.fourierLabel.raise_()
        self.resampleSpinBox.raise_()
        self.resampleLabel.raise_()
        self.fourierOpt.raise_()
        self.optYes.raise_()
        self.optNot.raise_()
        self.displayFramesOpt.raise_()
        self.dispOptNot.raise_()
        self.dispOptYes.raise_()
        self.displayFramesLabel.raise_()
        contraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(contraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 21))
        self.menubar.setObjectName("menubar")
        contraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(contraWindow)
        self.statusbar.setObjectName("statusbar")
        contraWindow.setStatusBar(self.statusbar)

        self.retranslateUi(contraWindow)
        QtCore.QMetaObject.connectSlotsByName(contraWindow)
        
# Added ================       
 
        self.initiateWidgets()

# =====================

    def retranslateUi(self, contraWindow):
        _translate = QtCore.QCoreApplication.translate
        contraWindow.setWindowTitle(_translate("contraWindow", "MainWindow"))
        self.titleLabel.setText(_translate("contraWindow", "conduXer<sup>2</sup>: Contraction + Fourier Analysis"))
        self.inputFileLabel.setText(_translate("contraWindow", "Input File:"))
        self.browseButton.setText(_translate("contraWindow", "Browse"))
        self.fpsLabel.setText(_translate("contraWindow", "Frame Rate (fps):"))
        self.fpsEntry.setText(_translate("contraWindow", "30"))
        self.runButton.setText(_translate("contraWindow", "RUN"))
        self.fourierLabel.setText(_translate("contraWindow", "Fourier Analysis?"))
        self.resampleLabel.setText(_translate("contraWindow", "Re-Sampling Factor:"))
        self.optYes.setText(_translate("contraWindow", "Yes"))
        self.optNot.setText(_translate("contraWindow", "No"))
        self.dispOptNot.setText(_translate("contraWindow", "No"))
        self.dispOptYes.setText(_translate("contraWindow", "Yes"))
        self.displayFramesLabel.setText(_translate("contraWindow", "Display Frames?"))
        
 # Added ===========
        
    def initiateWidgets(self):
        self.browseButton.clicked.connect(self.openFileBrowser)
        self.runButton.clicked.connect(self.mainContraFunction)

        
    def openFileBrowser(self):   
        global inFile
        options = QtWidgets.QFileDialog.Options()
#        options |= QtWidgets.QFileDialog.DontUseNativeDialog
#        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select STM File", "", "TIFF Files (*.tif *.png)", options=options)
        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Contraction Video File", "", "Video Files (*.avi)", options=options)
#        if inFile:
#            print(inFile)
        self.inputFileEntry.addItem(inFile)
        del options

    def mainContraFunction(self):      
        
        global fps, fSp, cid, currCoords, roiCoords, fourierOption, displayOption, resampleFactor, directory, rootVideoName      
        
        fps = int(self.fpsEntry.text())
        fourierOption = self.fourierOpt.value()
        displayOption = self.displayFramesOpt.value()
        resampleFactor = int(self.resampleSpinBox.value())

        videoName = inFile.split("/")[-1]
        directory = inFile[:-len(videoName)]+'/'+videoName[:-4]
        rootVideoName = videoName[:-4]

        if not os.path.exists(directory):
            os.makedirs(directory)
        
        try:
            cap = cv2.VideoCapture(inFile)
        except:
            print 'Error Loading Video File'

        ret, singleFrame = cap.read()
        cap.release()       

        fSp = plt.figure(figsize=(16,8))
        ax = fSp.add_subplot(111)
        ax.imshow(singleFrame,cmap='gray')
        
        currCoords = []
        roiCoords = []

        cid = fSp.canvas.mpl_connect('button_press_event', self.contraROI)

        plt.show()
        
    def contraROI(self,event):
       
        xROICoord, yROICoord = event.xdata, event.ydata

        myROICoords = []

        myROICoords.append((xROICoord,yROICoord))
        roiCoords.append(myROICoords)
      
        if len(roiCoords) == 4:
            fSp.canvas.mpl_disconnect(cid)
            plt.close(fSp)

            firstROICoords = np.transpose(np.asarray(roiCoords[0]))
            secondROICoords = np.transpose(np.asarray(roiCoords[1]))
            thirdROICoords = np.transpose(np.asarray(roiCoords[2]))
            fourthROICoords = np.transpose(np.asarray(roiCoords[3]))

            global roiUnoCx, roiDosCx, roiUnoCy, roiDosCy

            r1x = int(firstROICoords[0])
            r2x = int(secondROICoords[0])
            r3x = int(thirdROICoords[0])
            r4x = int(fourthROICoords[0])

            r1y = int(firstROICoords[1])
            r2y = int(secondROICoords[1])
            r3y = int(thirdROICoords[1])
            r4y = int(fourthROICoords[1])      
            
            roiUnoCx = min(r1x, r2x, r3x, r4x)
            roiDosCx = max(r1x, r2x, r3x, r4x)
            roiUnoCy = min(r1y, r2y, r3y, r4y)
            roiDosCy = max(r1y, r2y, r3y, r4y)         
            
#            time.sleep(5)
            
            self.contraVideoReader(inFile, fps)  



    def contraVideoReader(self, inVideo, fps):
        
        try:
            cap = cv2.VideoCapture(inVideo)
        except:
            print 'Error Loading Video File'

        ret, singleFrame = cap.read()
        totalFrames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
        cap.release()

        singleFrame = singleFrame[roiUnoCy:roiDosCy,roiUnoCx:roiDosCx]

        frameSize = singleFrame.shape # [height, width]

        frH = frameSize[0]
        frW = frameSize[1]

        if displayOption == 1:
            videoFrames = "Displaying Video Frames"
            cv2.namedWindow(videoFrames, cv2.CV_WINDOW_AUTOSIZE)
            cv2.startWindowThread()

        cap = cv2.VideoCapture(inVideo)

        vesselOD = [[] for i in range(frW)]

        counter = 0

        while(cap.isOpened()):
            ret, fullFrame = cap.read()
            if(ret==True):
                frame = fullFrame[roiUnoCy:roiDosCy,roiUnoCx:roiDosCx]
                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converting to GrayScale
                blurFrame = cv2.GaussianBlur(grayFrame,(3,3),0)
                ret,threshFrame = cv2.threshold(blurFrame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                grayInvFrame = cv2.bitwise_not(threshFrame) # Inverting Scale - Black=255
#                threshFrame = cv2.adaptiveThreshold(grayFrame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,45,0)
#                kernelT = np.ones((5,5),np.uint8)
##                openContourFrame = cv2.morphologyEx(contourFrame, cv2.MORPH_OPEN, kernel)
#                closeFrame = cv2.morphologyEx(threshFrame, cv2.MORPH_CLOSE, kernelT)
##                grayFrBlur = cv2.GaussianBlur(grayInvFrame,(3,3),0) # Smoothing Image (Blur)
#                retGray, threshFrame = cv2.threshold(grayInvFrame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # Use THRESH_BINARY_INV if the background is white
                contours, hierarchy = cv2.findContours(grayInvFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                sortContours = sorted(contours, key=cv2.contourArea, reverse=True)

                contourFrame = np.zeros(grayFrame.shape,np.uint8)
#                cv2.drawContours(contourFrame, sortContours, -1, (255,0,0), -1)
                nCnts = len(sortContours)
                thrCnt = 0

                for c in range(0,nCnts):
                    if cv2.contourArea(sortContours[c]) > 10.:
                        thrCnt = thrCnt+1
                
                cv2.drawContours(contourFrame, sortContours[0:thrCnt], -1, (255,0,0), -1)

                kernel = np.ones((3,3),np.uint8)
#                openContourFrame = cv2.morphologyEx(contourFrame, cv2.MORPH_OPEN, kernel)
                closeContourFrame = cv2.morphologyEx(contourFrame, cv2.MORPH_CLOSE, kernel)

                contourFrame = closeContourFrame

                if displayOption == 1:
                    wallFrames = np.concatenate((grayFrame, contourFrame),axis=0)
                    cv2.imshow(videoFrames,wallFrames)

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

                for k in range(0,frW):
                    oneLine = contourFrame[:,k]
                    edges = cv2.Canny(oneLine,100,255)
                    wallEdges = np.nonzero(edges)[0]
                    if len(wallEdges) >= 2:
                        currentOD = wallEdges[-1]-wallEdges[0]
                    else:
                        currentOD = 0
                      
                    vesselOD[k].append(currentOD)
                                         
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
            else:
                cap.release()
                cv2.destroyWindow('videoFrames')
                cv2.waitKey(1)

##        print time.strftime("%H:%M:%S")


        ODTime = np.asarray(vesselOD).astype('float64')
        ODTime = ODTime[1:-1,:]

#        lnODTime = ODTime.shape[0]
#        nFODTime = ODTime.shape[1]
#
#        tmpPixLoc = np.zeros(5,'int')
#
#        tmpPixLoc[0] = int(0.05*lnODTime)
#        tmpPixLoc[4] = int(0.95*lnODTime)
#
#        gapLoc5 = int((tmpPixLoc[4]-tmpPixLoc[0])/4)
#
#        selODTime = np.zeros(shape=(5,nFODTime))
#
#        for t in range(0,5):
#            if t > 0 and t < 4:
#                tmpPixLoc[t] = int(tmpPixLoc[0]+int(gapLoc5*t))
#            tmpADD = np.zeros(shape=(1,nFODTime))
#            counterTemp = 0
#            for p in range(0,5):
#                counterTemp = counterTemp + 1
#                tmpADD = np.add(tmpADD,ODTime[(tmpPixLoc[t]-2)+p])
#            selODTime[t] = tmpADD/counterTemp
#
#        timeArray = np.arange(float(nFODTime))
#        timeArray = timeArray/fps

#        tpTimeArray = np.transpose(timeArray)
#
#        tpSelODTime = np.transpose(selODTime)
        
##        OD2Write = np.concatenate((np.transpose(timeArray),tpSelODTime),axis=0)
#        np.savetxt(inFile[:-4]+"_selectedODLocations_v5p1.txt", tpSelODTime, fmt='%10.8f', delimiter=" ")
      
        
##        fltODTime = np.zeros(shape=(ODTime.shape[0],ODTime.shape[1]),dtype=float)
        
##        for m in range(0,ODTime.shape[0]):
##            fltODTime[m,:] = self.savitzky_golay(ODTime[m,:], 51, 5)
##
##        nfrms = np.arange(ODTime.shape[1])
##        sampleOD = ODTime[int(ODTime.shape[0]/2)+10,:]
##        fltsampleOD = self.savitzky_golay(sampleOD, 51, 5)
##
##        fTemporal = plt.figure(figsize=(16,8),frameon=False)
##        plt.subplot(311)
##        plt.plot(nfrms,sampleOD)
##        plt.subplot(312)
##        plt.plot(nfrms,fltsampleOD)
##        plt.subplot(313)
##        plt.plot(nfrms[:-2],np.diff(np.diff(fltsampleOD)))
##        plt.show()


              
##        for m in range(0,scanH):        

##        fltODTime = self.savitzky_golay(ODTime, 11, 5)

##        print ODTime.shape
##
##
##        print ODTime.shape

#        clipmax = frH-20
#        ODTime = np.clip(ODTime,0,clipmax)

        maxPix = np.amax(ODTime)
        
#        minPix = np.amin(ODTime[np.nonzero(ODTime)])
        minPix = np.amin(ODTime)
        
#        print 'All Min: ', minPix

#        if minPix <= 20:
#            minPix = 20
        
        ODTimeNorm = ((ODTime-minPix)/(maxPix-minPix))*255.
       
        ODTimeNorm = np.clip(ODTimeNorm,0,255)
        
        stmH = ODTimeNorm.shape[0]
        
        lineNormODTime = np.zeros(ODTime.shape, dtype=float)
        
        for l in range(0,stmH):
            lineMin = np.amin(ODTime[l,:])
            lineMax = np.amax(ODTime[l,:])
            lineNormODTime[l,:] = ((ODTime[l,:]-lineMin)/(lineMax-lineMin))*255.
        
        lineNormODTime = np.clip(lineNormODTime,0,255)
        
        global spaceTime

        spaceTime = ODTimeNorm.astype('uint8')
        spaceTime = np.flipud(spaceTime)
        lineSpaceTime = lineNormODTime.astype('uint8')
        lineSpaceTime = np.flipud(lineSpaceTime)
        
        ret,thrSpaceTime = cv2.threshold(lineSpaceTime,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        factoredSTM = spaceTime[:,0:totalFrames:resampleFactor]        
        
        np.savetxt(directory+'/'+rootVideoName+"_STMrawdata_conduXer2.txt", np.flipud(ODTime), fmt='%10.8f', delimiter=" ")

        try:
            imAVISTM = Image.fromarray(spaceTime)
            imAVISTM.save(directory+'/'+rootVideoName+'_STM_conduXer2.tif',compression = 'None')
            imAVISTM.save(directory+'/'+rootVideoName+'_STM_conduXer2.png',compression = 'None')
            imLineSTM = Image.fromarray(lineSpaceTime)
            imLineSTM.save(directory+'/'+rootVideoName+'_STM_LineByLine_conduXer2.tif',compression = 'None')
            imLineSTM.save(directory+'/'+rootVideoName+'_STM_LineByLine_conduXer2.png',compression = 'None')            
            imThSTM = Image.fromarray(thrSpaceTime)
            imThSTM.save(directory+'/'+rootVideoName+'_STM_Thresh_conduXer2.tif',compression = 'None')
            imThSTM.save(directory+'/'+rootVideoName+'_STM_Thresh_conduXer2.png',compression = 'None')
        except:
            print "Error Saving Full Resolution STM"

        if resampleFactor>1:
            try:
                imAVISTMfactor = Image.fromarray(factoredSTM)
                facLabel = '_factor'+str(resampleFactor)
                imAVISTMfactor.save(directory+'/'+rootVideoName+facLabel+'_conduXer2.tif',compression = 'None')
            except:
                print "Error Saving Resampled STM"      
        
        if fourierOption == 1:
            self.SFMapAnalysis()
         

    def SFMapAnalysis(self):

        oneFrame = 1/float(fps)

        stmLength = spaceTime.shape[1]

        if stmLength > 1:
            for i in range(2, stmLength):
                if (stmLength % i) == 0:
                    prime = 0
                    break
                else:
                    prime = 1

        if prime == 1:
            fullSTMap = spaceTime[:,:-1]
        
        del prime
        
        fullSTMap = spaceTime
        tfullSTMap = np.transpose(fullSTMap)

        freqCut = 1.
             
        fftSTMap = np.fft.fft(tfullSTMap,axis=0)

        fftSTMap2 = abs(fftSTMap**2)

        freqDomain = np.fft.fftfreq(tfullSTMap.shape[0],oneFrame)
        freqDomain = freqDomain*60
      
        freqStep = abs(freqDomain[1]-freqDomain[0])
        freqLimIndex = int(30/freqStep)
        
        # Selecting only positive frequencies below 30 contractions/minute

        roiFreqSTMap2 = fftSTMap2[0:freqLimIndex,:] 
        roiFreqDom = freqDomain[0:freqLimIndex] # 1-->20

        for p in range(0,int(np.ceil(freqCut/freqStep))):
            roiFreqSTMap2[p,:]=0      

        # --------------------------------------------------
        # Normalizing array to display as 8-bit image

        freqMap = roiFreqSTMap2.astype('float64')

        maxFreq = np.amax(freqMap)
        minFreq = np.amin(freqMap)
        freqMapNorm = ((freqMap-minFreq)/(maxFreq-minFreq))*255.
        freqSpaceMap = freqMapNorm.astype('uint8')      

        oSize = freqSpaceMap.shape[0]

        if oSize < 900:
            imScale = np.ceil(900/oSize)
        else:
            imScale = 1
               
        imFSM = Image.fromarray(np.rot90(freqSpaceMap))
        imFSM.save(directory+'/'+rootVideoName+'_SFM_conduXer2.tif',compression = 'None')
#        origFSM = cv2.imread(directory+'/'+rootVideoName+'_SFM_conduXer2.tif',0)
        resFSM = cv2.resize(freqSpaceMap,None,fx=1,fy=imScale,interpolation=cv2.INTER_CUBIC)
        resimFSM = Image.fromarray(np.rot90(np.asarray(resFSM.astype('uint8'))))
        resimFSM.save(directory+'/'+rootVideoName+'_scaledSFM_conduXer2.tif',compression = 'None')
                
        # --------------------------------------------------

        sumROIFreqMap = np.sum(freqMap,axis=1)
        sumScaledROIFreqMap = np.sum(resFSM,axis=1)

##        minROIfreq = np.amin(roiFreqDom)

##        ytickPos = np.arange(0,100,10/freqStep)
##        ylabels = np.arange(0,100,10)
##
##        fSp = plt.figure(figsize=(16,8))
##        ax = fSp.add_subplot(111)
##        imData = ax.imshow(freqSpaceMap,cmap='gray') 
####        plt.axes().set_aspect(30)
##        plt.tick_params(
##            axis='x',          # changes apply to the x-axis
##            which='both',      # both major and minor ticks are affected
##            bottom='off',      # ticks along the bottom edge are off
##            top='off',         # ticks along the top edge are off
##            labelbottom='off') # labels along the bottom edge are off
##        ax.set_yticks(ytickPos)
##        ax.set_yticklabels(ylabels)
##        plt.ylim((0,30))
##        plt.ylabel('Frequency (contractions/minute)')



        sumFreqStack = np.append([np.transpose(roiFreqDom)],[np.transpose(sumROIFreqMap)],axis=0)
        sumFreqStack = np.transpose(sumFreqStack)

        scaledBin = (np.amax(roiFreqDom)-np.amin(roiFreqDom))/resFSM.shape[0]
        scaledFreqDom = np.transpose(np.arange(np.amin(roiFreqDom),np.amax(roiFreqDom),scaledBin))
        
        sumScaledROIFreqMap = sumScaledROIFreqMap/float(np.amax(sumScaledROIFreqMap))
        scaledSumFreqStack = np.append([scaledFreqDom],[np.transpose(sumScaledROIFreqMap)],axis=0)
        scaledSumFreqStack = np.transpose(scaledSumFreqStack)

#        fDos = plt.figure(figsize=(16,8),frameon=False)       
#        plt.plot(scaledFreqDom,sumScaledROIFreqMap)
#        plt.xlabel('Frequency (Contractions/Minute)')
#        fDos.savefig(directory+'/'+rootVideoName+'_SFMhisto_conduXer2.png', bbox_inches='tight', pad_inches=0)
#        ##plt.xlim((1,100))
#        ##plt.ylim((0,1e10))


#        np.savetxt(directory+'/'+rootVideoName+"_sumFreqDistribution_conduXer2.txt", sumFreqStack, fmt='%10.8f', delimiter=" ")
        np.savetxt(directory+'/'+rootVideoName+"_scaled_sumFreqDistribution_conduXer2.txt", scaledSumFreqStack, fmt='%10.8f', delimiter=" ")

##        subprocess.call("cls", shell=True)
        tempStr = "Fourier Analysis Completed"
        subprocess.call(["echo", tempStr], shell=True)

##        plt.show()




# =====================       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    contraWindow = QtWidgets.QMainWindow()
    ui = Ui_contraWindow()
    ui.setupContraUi(contraWindow)
    contraWindow.show()
    sys.exit(app.exec_())

