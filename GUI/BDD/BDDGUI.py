# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BDDGUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BDDGui(object):
    def setupUi(self, BDDGui):
        BDDGui.setObjectName("BDDGui")
        BDDGui.resize(681, 509)
        self.centralwidget = QtWidgets.QWidget(BDDGui)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(55, 115, 171);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.numOfVarsEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numOfVarsEdit.setFont(font)
        self.numOfVarsEdit.setStyleSheet("color: rgb(38, 78, 117);")
        self.numOfVarsEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.numOfVarsEdit.setObjectName("numOfVarsEdit")
        self.horizontalLayout_2.addWidget(self.numOfVarsEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(55, 115, 171);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.orderOfVarsEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.orderOfVarsEdit.setFont(font)
        self.orderOfVarsEdit.setStyleSheet("color: rgb(38, 78, 117);")
        self.orderOfVarsEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.orderOfVarsEdit.setObjectName("orderOfVarsEdit")
        self.horizontalLayout_4.addWidget(self.orderOfVarsEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(55, 115, 171);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.functionEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.functionEdit.setFont(font)
        self.functionEdit.setStyleSheet("color: rgb(38, 78, 117);")
        self.functionEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.functionEdit.setObjectName("functionEdit")
        self.horizontalLayout_5.addWidget(self.functionEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.problemChecker = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        self.problemChecker.setFont(font)
        self.problemChecker.setObjectName("problemChecker")
        self.horizontalLayout_6.addWidget(self.problemChecker)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.solveButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.solveButton.setObjectName("solveButton")
        self.verticalLayout_2.addWidget(self.solveButton)
        self.clearButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_2.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bddTreeView = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.bddTreeView.setFont(font)
        self.bddTreeView.setStyleSheet("color: rgb(55, 115, 171);")
        self.bddTreeView.setObjectName("bddTreeView")
        self.verticalLayout_3.addWidget(self.bddTreeView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        BDDGui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BDDGui)
        self.statusbar.setObjectName("statusbar")
        BDDGui.setStatusBar(self.statusbar)

        self.retranslateUi(BDDGui)
        QtCore.QMetaObject.connectSlotsByName(BDDGui)

    def retranslateUi(self, BDDGui):
        _translate = QtCore.QCoreApplication.translate
        BDDGui.setWindowTitle(_translate("BDDGui", "BDD Solver"))
        self.label_2.setText(_translate("BDDGui", "Give the number of vars: "))
        self.label_5.setText(_translate("BDDGui", "Give the number of variables the function will have "))
        self.label_3.setText(_translate("BDDGui", "Give the order of vars: "))
        self.label_6.setText(_translate("BDDGui", "Example: (x < y < z) for 3 variables"))
        self.label_4.setText(_translate("BDDGui", "Give the function: "))
        self.label_7.setText(_translate("BDDGui", "Example: (x + y\' + z) for 3 variables"))
        self.problemChecker.setText(_translate("BDDGui", "Problem"))
        self.solveButton.setText(_translate("BDDGui", "Solve"))
        self.clearButton.setText(_translate("BDDGui", "Clear"))
        self.bddTreeView.setText(_translate("BDDGui", "Here your bdd result will appear."))