# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_database_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditDatabaseItemWindow(object):
    def setupUi(self, EditDatabaseItemWindow):
        EditDatabaseItemWindow.setObjectName("EditDatabaseItemWindow")
        EditDatabaseItemWindow.resize(513, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditDatabaseItemWindow.sizePolicy().hasHeightForWidth())
        EditDatabaseItemWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(EditDatabaseItemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(120, 210, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 110, 331, 61))
        self.lineEdit.setObjectName("lineEdit")
        EditDatabaseItemWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditDatabaseItemWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        EditDatabaseItemWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EditDatabaseItemWindow)
        self.statusbar.setObjectName("statusbar")
        EditDatabaseItemWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(EditDatabaseItemWindow)
        QtCore.QMetaObject.connectSlotsByName(EditDatabaseItemWindow)

    def retranslateUi(self, EditDatabaseItemWindow):
        _translate = QtCore.QCoreApplication.translate
        EditDatabaseItemWindow.setWindowTitle(_translate("EditDatabaseItemWindow", "MainWindow"))
        self.label.setText(_translate("EditDatabaseItemWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Edit</span></p></body></html>"))
        self.saveBtn.setText(_translate("EditDatabaseItemWindow", "Save"))
        self.menuInteractive_System_Modelling.setTitle(_translate("EditDatabaseItemWindow", "1"))
