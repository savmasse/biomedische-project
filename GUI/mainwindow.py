# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SamVa\Desktop\UGent\Biomedische\GUI\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 801, 551))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblQuestion = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblQuestion.setObjectName(_fromUtf8("lblQuestion"))
        self.verticalLayout.addWidget(self.lblQuestion)
        self.graphicsView = PlotWidget(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.leditAnswer = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.leditAnswer.setObjectName(_fromUtf8("leditAnswer"))
        self.verticalLayout.addWidget(self.leditAnswer)
        self.btnSubmit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnSubmit.setObjectName(_fromUtf8("btnSubmit"))
        self.verticalLayout.addWidget(self.btnSubmit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNew_session = QtGui.QAction(MainWindow)
        self.actionNew_session.setObjectName(_fromUtf8("actionNew_session"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionOpen_DB = QtGui.QAction(MainWindow)
        self.actionOpen_DB.setObjectName(_fromUtf8("actionOpen_DB"))
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionNew_session)
        self.menuFile.addAction(self.actionOpen_DB)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lblQuestion.setText(_translate("MainWindow", "Question #1", None))
        self.btnSubmit.setText(_translate("MainWindow", "Submit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNew_session.setText(_translate("MainWindow", "Start session", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionOpen_DB.setText(_translate("MainWindow", "Open DB", None))

from pyqtgraph import PlotWidget
