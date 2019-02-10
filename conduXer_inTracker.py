# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer_inTracker.ui'
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
import matplotlib.patches as patches
from math import factorial



class Ui_trackerWindow(object):
    def setupTrackerUi(self, trackerWindow):
        trackerWindow.setObjectName("trackerWindow")
        trackerWindow.resize(920, 518)
        self.centralwidget = QtWidgets.QWidget(trackerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(160, 10, 591, 51))
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
        self.fpsLabel.setGeometry(QtCore.QRect(30, 310, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fpsEntry.setGeometry(QtCore.QRect(200, 300, 41, 41))
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
        self.runButton.setGeometry(QtCore.QRect(710, 400, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 70, 921, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/tracker.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.calibLabel = QtWidgets.QLabel(self.centralwidget)
        self.calibLabel.setGeometry(QtCore.QRect(280, 310, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.calibLabel.setFont(font)
        self.calibLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.calibLabel.setObjectName("calibLabel")
        self.displayFramesOpt = QtWidgets.QSlider(self.centralwidget)
        self.displayFramesOpt.setGeometry(QtCore.QRect(810, 300, 71, 41))
        self.displayFramesOpt.setMaximum(1)
        self.displayFramesOpt.setSliderPosition(0)
        self.displayFramesOpt.setOrientation(QtCore.Qt.Horizontal)
        self.displayFramesOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.displayFramesOpt.setObjectName("displayFramesOpt")
        self.dispOptNot = QtWidgets.QLabel(self.centralwidget)
        self.dispOptNot.setGeometry(QtCore.QRect(790, 270, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptNot.setFont(font)
        self.dispOptNot.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptNot.setObjectName("dispOptNot")
        self.dispOptYes = QtWidgets.QLabel(self.centralwidget)
        self.dispOptYes.setGeometry(QtCore.QRect(860, 270, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.dispOptYes.setFont(font)
        self.dispOptYes.setAlignment(QtCore.Qt.AlignCenter)
        self.dispOptYes.setObjectName("dispOptYes")
        self.displayFramesLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayFramesLabel.setGeometry(QtCore.QRect(620, 310, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.displayFramesLabel.setFont(font)
        self.displayFramesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.displayFramesLabel.setObjectName("displayFramesLabel")
        self.calibEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.calibEntry.setGeometry(QtCore.QRect(500, 300, 71, 41))
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
        trackerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(trackerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        trackerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(trackerWindow)
        self.statusbar.setObjectName("statusbar")
        trackerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(trackerWindow)
        QtCore.QMetaObject.connectSlotsByName(trackerWindow)

# Added ================       
 
        self.initiateWidgets()

# =====================

    def retranslateUi(self, trackerWindow):
        _translate = QtCore.QCoreApplication.translate
        trackerWindow.setWindowTitle(_translate("trackerWindow", "MainWindow"))
        self.titleLabel.setText(_translate("trackerWindow", "conduXer<sup>2</sup>: Inner-Diameter Tracking"))
        self.inputFileLabel.setText(_translate("trackerWindow", "Input File:"))
        self.browseButton.setText(_translate("trackerWindow", "Browse"))
        self.fpsLabel.setText(_translate("trackerWindow", "Frame Rate (fps):"))
        self.fpsEntry.setText(_translate("trackerWindow", "30"))
        self.runButton.setText(_translate("trackerWindow", "RUN"))
        self.calibLabel.setText(_translate("trackerWindow", "Calibration (um/pixel):"))
        self.dispOptNot.setText(_translate("trackerWindow", "No"))
        self.dispOptYes.setText(_translate("trackerWindow", "Yes"))
        self.displayFramesLabel.setText(_translate("trackerWindow", "Display Frames?"))
        self.calibEntry.setText(_translate("trackerWindow", "1.40"))

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
        if inFile:
            print(inFile)
        self.inputFileEntry.addItem(inFile)
        del options

    def mainContraFunction(self):      
        
        global fps, fSp, cid, currCoords, roiCoords, fourierOption, displayOption, resampleFactor, directory, rootVideoName      
        
        fps = int(self.fpsEntry.text())
        displayOption = self.displayFramesOpt.value()

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
      
        if len(roiCoords) == 2:
            fSp.canvas.mpl_disconnect(cid)
            plt.close(fSp)

            firstROICoords = np.transpose(np.asarray(roiCoords[0]))
            secondROICoords = np.transpose(np.asarray(roiCoords[1]))
#            thirdROICoords = np.transpose(np.asarray(roiCoords[2]))
#            fourthROICoords = np.transpose(np.asarray(roiCoords[3]))

            global roiUnoCx, roiDosCx, roiUnoCy, roiDosCy

            r1x = int(firstROICoords[0])
            r2x = int(secondROICoords[0])
#            r3x = int(thirdROICoords[0])
#            r4x = int(fourthROICoords[0])

            r1y = int(firstROICoords[1])
            r2y = int(secondROICoords[1])
#            r3y = int(thirdROICoords[1])
#            r4y = int(fourthROICoords[1])      
            
            roiUnoCx = min(r1x, r2x)
            roiDosCx = max(r1x, r2x)
#            roiUnoCy = min(r1y, r2y, r3y, r4y)
#            roiDosCy = max(r1y, r2y, r3y, r4y)         
            
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

        singleFrame = singleFrame[:,roiUnoCx:roiDosCx]

        frameSize = singleFrame.shape # [height, width]

        frH = frameSize[0]
        frW = frameSize[1]

        if displayOption == 1:
            videoFrames = "Displaying Video Frames"
            cv2.namedWindow(videoFrames, cv2.CV_WINDOW_AUTOSIZE)
            cv2.startWindowThread()

        cap = cv2.VideoCapture(inVideo)

        vesselOD = [[] for i in range(frW)]
        topID = np.zeros(frW, dtype=int)
        bottomID = np.zeros(frW, dtype=int)

        counter = 0

        while(cap.isOpened()):
            ret, fullFrame = cap.read()
            if(ret==True):
                fullGrayFrame = cv2.cvtColor(fullFrame, cv2.COLOR_BGR2GRAY) # Converting to GrayScale
                grayFrame = fullGrayFrame[:,roiUnoCx:roiDosCx]
                trackFrame = cv2.cvtColor(fullFrame, cv2.COLOR_BGR2GRAY) # Converting to GrayScale
                grayInvFrame = cv2.bitwise_not(grayFrame) # Inverting Scale - Black=255
                grayFrBlur = cv2.GaussianBlur(grayInvFrame,(5,5),0) # Smoothing Image (Blur)
                retGray, threshFrame = cv2.threshold(grayFrBlur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # Use THRESH_BINARY_INV if the background is white
                contours, hierarchy = cv2.findContours(threshFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                sortContours = sorted(contours, key=cv2.contourArea, reverse=True)
                vesselWalls = sortContours[0:2]
                    
                contourFrame = np.zeros(grayFrame.shape,np.uint8)
                cv2.drawContours(contourFrame, vesselWalls, -1, (255,0,0), -1)
                contourFrame = cv2.bitwise_not(contourFrame)

                Ct = 0
#                idEdgeTop = 0.
#                idEdgeBottom = 0.
                
                for k in range(0,frW):
                    oneLine = contourFrame[:,k]
                    edges = cv2.Canny(oneLine,100,255)
                    wallEdges = np.nonzero(edges)[0]
                    if len(wallEdges) >= 4:
                        Ct = Ct + 1
#                        idEdgeTop = idEdgeTop+wallEdges[1]
#                        idEdgeBottom = idEdgeBottom+wallEdges[-2]
                        currentOD = wallEdges[-1]-wallEdges[0]
                        bottomEdge = wallEdges[-2]
                        topEdge = wallEdges[1]
                        # Add average of currentID
                    else:
                        currentOD = 0
                        bottomEdge = 0
                        topEdge = 0
                      
                    vesselOD[k].append(currentOD)
                    bottomID[k] = bottomEdge
                    topID[k] = topEdge
                
                              
                idEdgesTop = topID[np.nonzero(topID)]
#                idEdgesTop = self.savitzky_golay(idEdgesTop,131,5)
                idEdgeTop = int(np.amin(idEdgesTop))
                
                idEdgesBottom = bottomID[np.nonzero(bottomID)]
#                idEdgesBottom = self.savitzky_golay(idEdgesBottom,131,5)
                idEdgeBottom = int(np.amax(idEdgesBottom))
                
#                print 'Top: ', idEdgesTop 
#                print 'Bottom', idEdgesBottom
#                idEdgeTop = int(idEdgeTop/Ct)
#                idEdgeBottom = int(idEdgeBottom/Ct)
                
                if displayOption == 1:
                    fullGrayFrame[:,roiUnoCx:roiDosCx] = contourFrame
                    cv2.rectangle(fullGrayFrame,(roiUnoCx,10),(roiDosCx,frH-10),(0,255,0),2)
                    cv2.rectangle(trackFrame,(roiUnoCx,10),(roiDosCx,frH-10),(0,255,0),2)
                    cv2.line(trackFrame,(roiUnoCx-15,idEdgeTop),(roiDosCx+15,idEdgeTop),(0,255,0),2)
                    cv2.line(trackFrame,(roiUnoCx-15,idEdgeBottom),(roiDosCx+15,idEdgeBottom),(0,255,0),2)
                    
                    wallFrames = np.concatenate((fullGrayFrame, trackFrame),axis=0)
                    cv2.imshow(videoFrames,wallFrames)

                counter = counter + 1
                                         
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
            else:
                cap.release()
                cv2.destroyWindow('videoFrames')
                cv2.waitKey(1)


#        ODTime = np.asarray(vesselOD).astype('float64')
#        ODTime = ODTime[1:-1,:]
#
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
#
#
#
#        clipmax = frH-20
#        ODTime = np.clip(ODTime,0,clipmax)
#
#        maxPix = np.amax(ODTime)
#        
#        minPix = np.amin(ODTime[np.nonzero(ODTime)])
#
#        if minPix <= 20:
#            minPix = 20
#        
#        ODTimeNorm = ((ODTime-minPix)/(maxPix-minPix))*255
#       
#        ODTimeNorm = np.clip(ODTimeNorm,0,255)
#
#        global spaceTime
#
#        spaceTime = ODTimeNorm.astype('uint8')
#        spaceTime = np.flipud(spaceTime)
#               
#        np.savetxt(directory+'/'+rootVideoName+"_STMrawdata_conduXer2.txt", np.flipud(ODTime), fmt='%10.8f', delimiter=" ")

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
    trackerWindow = QtWidgets.QMainWindow()
    ui = Ui_trackerWindow()
    ui.setupTrackerUi(trackerWindow)
    trackerWindow.show()
    sys.exit(app.exec_())

