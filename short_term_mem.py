# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'short_term_mem.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShortTermMemWindow(object):
    def setupUi(self, ShortTermMemWindow):
        ShortTermMemWindow.setObjectName("ShortTermMemWindow")
        ShortTermMemWindow.resize(1159, 861)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShortTermMemWindow.sizePolicy().hasHeightForWidth())
        ShortTermMemWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ShortTermMemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 130, 151, 51))
        self.label_4.setObjectName("label_4")
        self.factsTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.factsTableWidget.setGeometry(QtCore.QRect(80, 180, 991, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.factsTableWidget.setFont(font)
        self.factsTableWidget.setLineWidth(1)
        self.factsTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.factsTableWidget.setShowGrid(True)
        self.factsTableWidget.setWordWrap(True)
        self.factsTableWidget.setCornerButtonEnabled(True)
        self.factsTableWidget.setObjectName("factsTableWidget")
        self.factsTableWidget.setColumnCount(3)
        self.factsTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.factsTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.factsTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.factsTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.factsTableWidget.setHorizontalHeaderItem(2, item)
        self.factsTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.factsTableWidget.horizontalHeader().setDefaultSectionSize(324)
        self.factsTableWidget.horizontalHeader().setMinimumSectionSize(71)
        self.factsTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.factsTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.factsTableWidget.verticalHeader().setDefaultSectionSize(26)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 351, 51))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 351, 51))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(510, 760, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(700, 760, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName("editBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(890, 760, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.questTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.questTableWidget.setGeometry(QtCore.QRect(80, 490, 991, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.questTableWidget.setFont(font)
        self.questTableWidget.setLineWidth(1)
        self.questTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.questTableWidget.setShowGrid(True)
        self.questTableWidget.setWordWrap(True)
        self.questTableWidget.setCornerButtonEnabled(True)
        self.questTableWidget.setObjectName("questTableWidget")
        self.questTableWidget.setColumnCount(3)
        self.questTableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.questTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.questTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.questTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.questTableWidget.setHorizontalHeaderItem(2, item)
        self.questTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.questTableWidget.horizontalHeader().setDefaultSectionSize(324)
        self.questTableWidget.horizontalHeader().setMinimumSectionSize(71)
        self.questTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.questTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.questTableWidget.verticalHeader().setDefaultSectionSize(26)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 440, 151, 51))
        self.label_5.setObjectName("label_5")
        self.factsTableWidget.raise_()
        self.label.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.addBtn.raise_()
        self.editBtn.raise_()
        self.deleteBtn.raise_()
        self.questTableWidget.raise_()
        self.label_5.raise_()
        ShortTermMemWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShortTermMemWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1159, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        ShortTermMemWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShortTermMemWindow)
        self.statusbar.setObjectName("statusbar")
        ShortTermMemWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(ShortTermMemWindow)
        QtCore.QMetaObject.connectSlotsByName(ShortTermMemWindow)

        self.version_id = QtWidgets.QLabel(self.centralwidget)
        self.version_id.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_id.setObjectName("version_id")

    def retranslateUi(self, ShortTermMemWindow):
        _translate = QtCore.QCoreApplication.translate
        ShortTermMemWindow.setWindowTitle(_translate("ShortTermMemWindow", "MainWindow"))
        self.label.setText(_translate("ShortTermMemWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Short-Term Memory</span></p></body></html>"))
        self.label_4.setText(_translate("ShortTermMemWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Facts</span></p></body></html>"))
        item = self.factsTableWidget.verticalHeaderItem(0)
        item.setText(_translate("ShortTermMemWindow", "1"))
        item = self.factsTableWidget.verticalHeaderItem(1)
        item.setText(_translate("ShortTermMemWindow", "2"))
        item = self.factsTableWidget.verticalHeaderItem(2)
        item.setText(_translate("ShortTermMemWindow", "3"))
        item = self.factsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ShortTermMemWindow", "Domain"))
        item = self.factsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ShortTermMemWindow", "Fact"))
        item = self.factsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ShortTermMemWindow", "Decay Time (sec)"))
        __sortingEnabled = self.factsTableWidget.isSortingEnabled()
        self.factsTableWidget.setSortingEnabled(False)
        self.factsTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("ShortTermMemWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Project: Animal-Dog</span></p></body></html>"))
        self.label_3.setText(_translate("ShortTermMemWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Version #1.1: New</span></p></body></html>"))
        self.addBtn.setText(_translate("ShortTermMemWindow", "Add"))
        self.editBtn.setText(_translate("ShortTermMemWindow", "Edit"))
        self.deleteBtn.setText(_translate("ShortTermMemWindow", "Delete"))
        item = self.questTableWidget.verticalHeaderItem(0)
        item.setText(_translate("ShortTermMemWindow", "1"))
        item = self.questTableWidget.verticalHeaderItem(1)
        item.setText(_translate("ShortTermMemWindow", "2"))
        item = self.questTableWidget.verticalHeaderItem(2)
        item.setText(_translate("ShortTermMemWindow", "3"))
        item = self.questTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ShortTermMemWindow", "Domain"))
        item = self.questTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ShortTermMemWindow", "Question"))
        item = self.questTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ShortTermMemWindow", "Decay Time (sec)"))
        __sortingEnabled = self.questTableWidget.isSortingEnabled()
        self.questTableWidget.setSortingEnabled(False)
        self.questTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("ShortTermMemWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Questions</span></p></body></html>"))
        self.menuInteractive_System_Modelling.setTitle(_translate("ShortTermMemWindow", "1"))


