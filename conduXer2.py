# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\conduXer2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from conduXer_contraFourier import Ui_contraWindow
from conduXer_fourierSpectrogram import Ui_fourierWindow
from conduXer_nirf import Ui_nirfWindow
from conduXer_fluostm import Ui_fluoWindow
from conduXer_conduction import Ui_conduWindow
from conduXer_inTracker import Ui_trackerWindow
from conduXer_caEventyzer import Ui_caEventWindow

class Ui_MainWindow(object):
    def openContraFourier(self):
        self.contraWindow = QtWidgets.QMainWindow()
        self.uiContra = Ui_contraWindow()
        self.uiContra.setupContraUi(self.contraWindow)
        self.contraWindow.show()

    def openFourierSpectrogram(self):
        self.fourierWindow = QtWidgets.QMainWindow()
        self.uiFourier = Ui_fourierWindow()
        self.uiFourier.setupFourierUi(self.fourierWindow)
        self.fourierWindow.show()

    def openInVivoNIRF(self):
        self.nirfWindow = QtWidgets.QMainWindow()
        self.uiNirf = Ui_nirfWindow()
        self.uiNirf.setupNirfUi(self.nirfWindow)
        self.nirfWindow.show()

    def openFluoSTM(self):
        self.fluoWindow = QtWidgets.QMainWindow()
        self.uiFluo = Ui_fluoWindow()
        self.uiFluo.setupFluoUi(self.fluoWindow)
        self.fluoWindow.show()
        
    def openConduction(self):
        self.conduWindow = QtWidgets.QMainWindow()
        self.uiCondu = Ui_conduWindow()
        self.uiCondu.setupConduUi(self.conduWindow)
        self.conduWindow.show()    

    def openInTracker(self):
        self.trackerWindow = QtWidgets.QMainWindow()
        self.uiTracker = Ui_trackerWindow()
        self.uiTracker.setupTrackerUi(self.trackerWindow)
        self.trackerWindow.show() 
        
    def openCaEventyzer(self):
        self.caEventWindow = QtWidgets.QMainWindow()
        self.uiCaEvent = Ui_caEventWindow()
        self.uiCaEvent.setupCaEventUi(self.caEventWindow)
        self.caEventWindow.show() 
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 601)
        MainWindow.setFixedSize(601,601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.contraButton = QtWidgets.QPushButton(self.centralwidget)
        self.contraButton.setGeometry(QtCore.QRect(30, 230, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.contraButton.setFont(font)
        self.contraButton.setObjectName("contraButton")
        self.contraButton.clicked.connect(self.openContraFourier)
        
        self.calciumButton = QtWidgets.QPushButton(self.centralwidget)
        self.calciumButton.setGeometry(QtCore.QRect(330, 330, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calciumButton.setFont(font)
        self.calciumButton.setObjectName("calciumButton")
        self.calciumButton.clicked.connect(self.openCaEventyzer)
        self.calciumButton.setEnabled(False)

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 581, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/img.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(20, 20, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.mainTitle.setFont(font)
        self.mainTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainTitle.setAutoFillBackground(False)
        self.mainTitle.setLineWidth(1)
        self.mainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTitle.setWordWrap(False)
        self.mainTitle.setObjectName("mainTitle")
        
        self.caFlashesButton = QtWidgets.QPushButton(self.centralwidget)
        self.caFlashesButton.setGeometry(QtCore.QRect(30, 330, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.caFlashesButton.setFont(font)
        self.caFlashesButton.setObjectName("caFlashesButton")
        self.caFlashesButton.clicked.connect(self.openFluoSTM)
        
        self.conducButton = QtWidgets.QPushButton(self.centralwidget)
        self.conducButton.setGeometry(QtCore.QRect(330, 230, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.conducButton.setFont(font)
        self.conducButton.setObjectName("conducButton")
        self.conducButton.clicked.connect(self.openConduction)
       
        self.apButton = QtWidgets.QPushButton(self.centralwidget)
        self.apButton.setGeometry(QtCore.QRect(30, 380, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.apButton.setFont(font)
        self.apButton.setObjectName("apButton")
        self.apButton.setEnabled(False)
        
        self.stmVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.stmVideoButton.setGeometry(QtCore.QRect(330, 380, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stmVideoButton.setFont(font)
        self.stmVideoButton.setObjectName("stmVideoButton")
        self.stmVideoButton.setEnabled(False)
 
       
        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(60, 90, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.authorLabel.setFont(font)
        self.authorLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.authorLabel.setAutoFillBackground(False)
        self.authorLabel.setLineWidth(1)
        self.authorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.authorLabel.setWordWrap(False)
        self.authorLabel.setObjectName("authorLabel")
        
        self.contraIDtrack = QtWidgets.QPushButton(self.centralwidget)
        self.contraIDtrack.setGeometry(QtCore.QRect(30, 280, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.contraIDtrack.setFont(font)
        self.contraIDtrack.setObjectName("contraIDtrack")
        self.contraIDtrack.clicked.connect(self.openInTracker)
        
        self.fourierSpectrogram = QtWidgets.QPushButton(self.centralwidget)
        self.fourierSpectrogram.setGeometry(QtCore.QRect(330, 280, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fourierSpectrogram.setFont(font)
        self.fourierSpectrogram.setObjectName("fourierSpectrogram")
        self.fourierSpectrogram.clicked.connect(self.openFourierSpectrogram)
        
        self.trimTrace = QtWidgets.QPushButton(self.centralwidget)
        self.trimTrace.setGeometry(QtCore.QRect(30, 430, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.trimTrace.setFont(font)
        self.trimTrace.setObjectName("trimTrace")
        self.trimTrace.setEnabled(False)        
        
        self.signalAnalyzer = QtWidgets.QPushButton(self.centralwidget)
        self.signalAnalyzer.setGeometry(QtCore.QRect(330, 430, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signalAnalyzer.setFont(font)
        self.signalAnalyzer.setObjectName("signalAnalyzer")
        self.signalAnalyzer.setEnabled(False)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 540, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.inVivo_nirf = QtWidgets.QPushButton(self.centralwidget)
        self.inVivo_nirf.setGeometry(QtCore.QRect(330, 480, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inVivo_nirf.setFont(font)
        self.inVivo_nirf.setObjectName("inVivo_nirf")
        self.inVivo_nirf.clicked.connect(self.openInVivoNIRF)
        
        self.inVivo_contra = QtWidgets.QPushButton(self.centralwidget)
        self.inVivo_contra.setGeometry(QtCore.QRect(30, 480, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inVivo_contra.setFont(font)
        self.inVivo_contra.setObjectName("inVivo_contra")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "conduXer2 - Data Analysis Tools"))
        self.contraButton.setText(_translate("MainWindow", "Contraction+Fourier Analysis"))
        self.calciumButton.setText(_translate("MainWindow", "Intracellular Ca2+ Analysis"))
        self.mainTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">conduXer</span><span style=\" color:#ffffff; vertical-align:super;\">2</span></p></body></html>"))
        self.caFlashesButton.setText(_translate("MainWindow", "Fluorescence Line-Scan"))
        self.conducButton.setText(_translate("MainWindow", "Conduction Analysis"))
        self.apButton.setText(_translate("MainWindow", "AP Analysis"))
        self.stmVideoButton.setText(_translate("MainWindow", "STM Video Maker"))
        self.authorLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff; vertical-align:super;\">by Jorge A. Castorena-Gonzalez</span></p></body></html>"))
        self.contraIDtrack.setText(_translate("MainWindow", "Internal Diameter Tracking"))
        self.fourierSpectrogram.setText(_translate("MainWindow", "Fourier+Spectrogram"))
        self.trimTrace.setText(_translate("MainWindow", "Trace Reading+Trimming"))
        self.signalAnalyzer.setText(_translate("MainWindow", "Signal Analysis"))
        self.label_2.setText(_translate("MainWindow", "Updated: 190207"))
        self.inVivo_nirf.setText(_translate("MainWindow", "In-Vivo NIRF"))
        self.inVivo_contra.setText(_translate("MainWindow", "In-Vivo Contractions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

