# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer_fourierSpectrogram.ui'
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
#import math

class Ui_fourierWindow(object):
    def setupFourierUi(self, fourierWindow):
        fourierWindow.setObjectName("fourierWindow")
        fourierWindow.resize(950, 530)
        fourierWindow.setFixedSize(950, 530)
        self.centralwidget = QtWidgets.QWidget(fourierWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(280, 20, 641, 51))
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
        self.fpsLabel.setGeometry(QtCore.QRect(30, 250, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.fpsLabel.setFont(font)
        self.fpsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fpsLabel.setObjectName("fpsLabel")
        self.fpsEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fpsEntry.setGeometry(QtCore.QRect(200, 240, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fpsEntry.sizePolicy().hasHeightForWidth())
        self.fpsEntry.setSizePolicy(sizePolicy)
        self.fpsEntry.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
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
        self.label.setPixmap(QtGui.QPixmap("images/171023_Prox1Cre_GCaMP6f_Pop_4x__scaledSFM_conduXer2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.spectrogramLabel = QtWidgets.QLabel(self.centralwidget)
        self.spectrogramLabel.setGeometry(QtCore.QRect(30, 340, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.spectrogramLabel.setFont(font)
        self.spectrogramLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spectrogramLabel.setObjectName("spectrogramLabel")
        self.spectrogramWindowLabel = QtWidgets.QLabel(self.centralwidget)
        self.spectrogramWindowLabel.setGeometry(QtCore.QRect(400, 340, 311, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.spectrogramWindowLabel.setFont(font)
        self.spectrogramWindowLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spectrogramWindowLabel.setObjectName("spectrogramWindowLabel")
        self.spectrogramOpt = QtWidgets.QSlider(self.centralwidget)
        self.spectrogramOpt.setGeometry(QtCore.QRect(250, 340, 71, 41))
        self.spectrogramOpt.setMaximum(1)
        self.spectrogramOpt.setSliderPosition(1)
        self.spectrogramOpt.setOrientation(QtCore.Qt.Horizontal)
        self.spectrogramOpt.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.spectrogramOpt.setObjectName("spectrogramOpt")
        self.optYes = QtWidgets.QLabel(self.centralwidget)
        self.optYes.setGeometry(QtCore.QRect(300, 310, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optYes.setFont(font)
        self.optYes.setAlignment(QtCore.Qt.AlignCenter)
        self.optYes.setObjectName("optYes")
        self.optNot = QtWidgets.QLabel(self.centralwidget)
        self.optNot.setGeometry(QtCore.QRect(230, 310, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.optNot.setFont(font)
        self.optNot.setAlignment(QtCore.Qt.AlignCenter)
        self.optNot.setObjectName("optNot")
        self.spectrogramWindow = QtWidgets.QLineEdit(self.centralwidget)
        self.spectrogramWindow.setGeometry(QtCore.QRect(710, 330, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrogramWindow.sizePolicy().hasHeightForWidth())
        self.spectrogramWindow.setSizePolicy(sizePolicy)
        self.spectrogramWindow.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.spectrogramWindow.setFont(font)
        self.spectrogramWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spectrogramWindow.setCursorPosition(1)
        self.spectrogramWindow.setObjectName("spectrogramWindow")
        self.inputFileLabel.raise_()
        self.inputFileEntry.raise_()
        self.browseButton.raise_()
        self.fpsLabel.raise_()
        self.fpsEntry.raise_()
        self.runButton.raise_()
        self.label.raise_()
        self.titleLabel.raise_()
        self.spectrogramLabel.raise_()
        self.spectrogramWindowLabel.raise_()
        self.spectrogramOpt.raise_()
        self.optYes.raise_()
        self.optNot.raise_()
        self.spectrogramWindow.raise_()
        fourierWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fourierWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 21))
        self.menubar.setObjectName("menubar")
        fourierWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fourierWindow)
        self.statusbar.setObjectName("statusbar")
        fourierWindow.setStatusBar(self.statusbar)

        self.retranslateUi(fourierWindow)
        QtCore.QMetaObject.connectSlotsByName(fourierWindow)
        
        # Added ================       
 
        self.initiateWidgets()

        # =====================


    def retranslateUi(self, fourierWindow):
        _translate = QtCore.QCoreApplication.translate
        fourierWindow.setWindowTitle(_translate("fourierWindow", "MainWindow"))
        self.titleLabel.setText(_translate("fourierWindow", "conduXer<sup>2</sup>: Fourier + Spectrogram Analysis"))
        self.inputFileLabel.setText(_translate("fourierWindow", "Input File:"))
        self.browseButton.setText(_translate("fourierWindow", "Browse"))
        self.fpsLabel.setText(_translate("fourierWindow", "Frame Rate (fps):"))
        self.fpsEntry.setText(_translate("fourierWindow", "30"))
        self.runButton.setText(_translate("fourierWindow", "RUN"))
        self.spectrogramLabel.setText(_translate("fourierWindow", "Create Spectrogram?"))
        self.spectrogramWindowLabel.setText(_translate("fourierWindow", "Spectrogram Window (minutes):"))
        self.optYes.setText(_translate("fourierWindow", "Yes"))
        self.optNot.setText(_translate("fourierWindow", "No"))
        self.spectrogramWindow.setText(_translate("fourierWindow", "1"))

 # Added ===========
        
    def initiateWidgets(self):
        self.browseButton.clicked.connect(self.openFileBrowser)
        self.runButton.clicked.connect(self.mainFourierFunction)

        
    def openFileBrowser(self):   
        global inFile
        options = QtWidgets.QFileDialog.Options()
#        options |= QtWidgets.QFileDialog.DontUseNativeDialog
#        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select STM File", "", "TIFF Files (*.tif *.png)", options=options)
        inFile, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Space-Time Map File", "", "TIF Files (*.tif)", options=options)
        if inFile:
            print(inFile)
        self.inputFileEntry.addItem(inFile)
        del options

    def mainFourierFunction(self):      
        
        global fps, fSp, cid, fourierOption, displayOption, resampleFactor, spectrogramOption     
        
        fps = int(self.fpsEntry.text())
        spectrogramOption = self.spectrogramOpt.value()
        specWindowWidth = float(self.spectrogramWindow.text())
        
        spaceTime = cv2.imread(inFile,0)
        
        NFFT = int(fps*60.)
        noverlap = int(fps*10)
        Fs = int(fps*60.)
        
        x = spaceTime[100,:]
        t = np.arange(int(spaceTime.shape[1]),dtype=int)
        
        fig, (ax1, ax2) = plt.subplots(nrows=2)
        ax1.plot(t, x)        
        Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=noverlap)
        plt.ylim((2,30))
        plt.show()
#        print im
#        print type(im)
#        plt.axis('off')
#        plt.imshow(im)
#        plt.plot(scaledFreqDom,sumScaledROIFreqMap)
#        plt.xlabel('Frequency (Contractions/Minute)')
        
        stmLength = spaceTime.shape[1]
       
        if stmLength > 1:
            for i in range(2, stmLength):
                if (stmLength % i) == 0:
                    prime = 0
                    break
                else:
                    prime = 1

        if prime == 1:
            spaceTime = spaceTime[:,:-1]
        
        del prime
        
        windowPix = int(np.ceil(specWindowWidth*60*fps))
        
        if windowPix > 1:
            for i in range(2, windowPix):
                if (windowPix % i) == 0:
                    prime = 0
                    break
                else:
                    prime = 1
        
        if prime == 1:
            windowPix = windowPix-1
            
        del prime
            
        stmLength = spaceTime.shape[1]
        numBlocks = int(np.ceil(float(stmLength)/float(windowPix)))
               
        global fileName, directory, histoDir, sfmDir, scaledDir, rootFileName
        
        fileName = inFile.split("/")[-1]
        directory = inFile[:-len(fileName)]+'/'+fileName[:-4]
        histoDir = directory+'/histograms'
        sfmDir = directory+'/sfm'
        scaledDir = sfmDir+'/scaled'
        rootFileName = fileName[:-4]
        
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.makedirs(histoDir)
            os.makedirs(sfmDir)
            os.makedirs(scaledDir)
            
        fileLabel = 'FullMap'    
            
        self.SFMapAnalysis(spaceTime,fileLabel)
        
        if spectrogramOption == 1:
            
            for k in range(0,numBlocks-1):
                try:
                    del fileName
                except:
                    pass
                infPix = k*windowPix
                supPix = (k+1)*windowPix
                if k==int(numBlocks-1):
                    supPix = stmLength
                fileLabel = '_win'+str(windowPix)+'_'+str(k+1)
                scaledFreqs, scaledDist = self.SFMapAnalysis(spaceTime[:,infPix:supPix],fileLabel)
                scaledDist = scaledDist*255.
                distLength = scaledDist.shape[0]
                scaledDistMap = np.reshape(scaledDist,(1,distLength))
                if k==0:
                    freqBins = scaledFreqs
                    freqTime = scaledDistMap
                if 0<k<numBlocks-1:
                    freqTime = np.concatenate((freqTime,scaledDistMap),axis=0)
                del scaledFreqs
                    
            freqTimeMap = np.rot90(freqTime.astype('uint8'))
                        
            ftScale = np.ceil(900./numBlocks-1)
            
            durationLabel = ((numBlocks-1)*windowPix)/fps
            
            imFSMTime = Image.fromarray(freqTimeMap)
            imFSMTime.save(directory+'/'+rootFileName+str(durationLabel)+'s_'+'_SFMTime.tif',compression = 'None')
            resFSMTime = cv2.resize(freqTimeMap,None,fx=ftScale,fy=1,interpolation=cv2.INTER_CUBIC)
            imResFSMTime = Image.fromarray(resFSMTime)
            imResFSMTime.save(directory+'/'+rootFileName+'_'+str(durationLabel)+'s_'+'_scaledSFMTime.tif',compression = 'None')
              
            rowSize = resFSMTime.shape[0]
            colSize = resFSMTime.shape[1]
            
            nMins = durationLabel/60. # Total Number of Minutes
            oneMin = int(np.ceil(colSize/nMins)) #pixels
            
            maxFreq = np.amax(freqBins)
            oneConMin = int(np.ceil(rowSize/maxFreq)) # pixels
            numFBins = int(maxFreq/2.) # number of 2-cont/min bins
            
#            timePos = np.arange(int(nMins))
#            timeLabels = map(str,np.arange(int(nMins)))
#            timePos = int(timePos*oneMin)
            
            fMain = plt.figure(figsize=(16,8),frameon=False)       
            plt.imshow(imResFSMTime, cmap='gist_rainbow')
            plt.xlabel('Time(minutes)',fontsize=18)
            plt.ylabel('Frequency (Contractions/Minute)',fontsize=18)
            plt.tick_params(labelsize=16)
            plt.xticks(np.arange(0,numBlocks*oneMin,step=oneMin),map(str,np.arange(int(numBlocks))))
            plt.yticks(np.arange(0,rowSize,step=int(oneConMin*2)),map(str,np.flip(np.arange((numFBins+2))*2,axis=0)))
            fMain.savefig(directory+'/'+rootFileName+'_SFMTimePlot.png', bbox_inches='tight', dpi=300, pad_inches=0.1)

            
    def SFMapAnalysis(self, fullSTMap, fileLabel):
        
        oneFrame = 1/float(fps)

        tfullSTMap = np.transpose(fullSTMap)

        freqCut = 0.5
               
        fftSTMap = np.fft.fft(tfullSTMap,axis=0)
        
        fftSTMap2 = abs(fftSTMap**2)

        freqDomain = np.fft.fftfreq(tfullSTMap.shape[0],oneFrame)
        freqDomain = freqDomain*60
      
        limitFreq = 30
        
        freqStep = abs(freqDomain[1]-freqDomain[0])
        freqLimIndex = int(limitFreq/freqStep) #Max Freq on SFM
        freqLimIndex = freqLimIndex+1
        
        # Selecting only positive frequencies below max contractions/minute

        roiFreqSTMap2 = fftSTMap2[0:freqLimIndex,:] 
        roiFreqDom = freqDomain[0:freqLimIndex] # 1-->20
        
        minFreqDom = np.amin(roiFreqDom)
        maxFreqDom = np.amax(roiFreqDom)
        
        for p in range(0,int(np.ceil(freqCut/freqStep))):
            roiFreqSTMap2[p,:]=0      

        # --------------------------------------------------
        # Normalizing array to display as 8-bit image

        freqMap = roiFreqSTMap2.astype('float64')

        maxFreq = np.amax(freqMap)
        minFreq = np.amin(freqMap)
        
        freqMapNorm = ((freqMap-minFreq)/(maxFreq-minFreq))*255.
        freqSpaceMap = np.rot90(freqMapNorm.astype('uint8'))      

        oSize = freqSpaceMap.shape[1]

        if oSize < 900:
            imScale = np.ceil(900./oSize)  
        else:
            imScale = 1
                     
        imFSM = Image.fromarray(freqSpaceMap)
        imFSM.save(sfmDir+'/'+rootFileName+fileLabel+'_SFM.tif',compression = 'None')
        resFSM = cv2.resize(freqSpaceMap,None,fx=imScale,fy=1,interpolation=cv2.INTER_CUBIC)
        resimFSM = Image.fromarray(np.asarray(resFSM.astype('uint8')))
        resimFSM.save(scaledDir+'/'+rootFileName+fileLabel+'_scaledSFM.tif',compression = 'None')
                
        # --------------------------------------------------
        
        sumROIFreqMap = np.sum(freqSpaceMap,axis=0)
        sumScaledROIFreqMap = np.sum(resFSM,axis=0)
        
        sumFreqStack = np.append([np.transpose(roiFreqDom)],[np.transpose(sumROIFreqMap)],axis=0)
        sumFreqStack = np.transpose(sumFreqStack)

        resizedWidth = resFSM.shape[1]

        scaledBin = (maxFreqDom-minFreqDom)/resizedWidth
               
        scaledFreqDom = np.transpose(np.arange(float(resizedWidth)))     
        scaledFreqDom = scaledFreqDom*scaledBin
                 
        sumScaledROIFreqMap = sumScaledROIFreqMap/float(np.amax(sumScaledROIFreqMap))
        
        scaledSumFreqStack = np.append([scaledFreqDom],[np.transpose(sumScaledROIFreqMap)],axis=0)
        scaledSumFreqStack = np.transpose(scaledSumFreqStack)

#        if fileLabel == 'FullMap':
#            fDos = plt.figure(figsize=(16,8),frameon=False)       
#            plt.plot(scaledFreqDom,sumScaledROIFreqMap)
#            plt.xlabel('Frequency (Contractions/Minute)')
#            fDos.savefig(histoDir+'/'+rootFileName+fileLabel+'_SFMhisto.png', bbox_inches='tight', pad_inches=0)

        np.savetxt(histoDir+'/'+rootFileName+fileLabel+"_sumFreqDist.txt", scaledSumFreqStack, fmt='%10.8f', delimiter=" ")

        tempStr = "Fourier Analysis Completed. Details: "+fileLabel
        subprocess.call(["echo", tempStr], shell=True)
        
        try:
            del fullSTMap
        except:
            pass
        
        return scaledFreqDom, sumScaledROIFreqMap

        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fourierWindow = QtWidgets.QMainWindow()
    ui = Ui_fourierWindow()
    ui.setupFourierUi(fourierWindow)
    fourierWindow.show()
    sys.exit(app.exec_())

