# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_fact_repr_in_sem_mem.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import MySQLdb as mdb
from contextlib import closing


class Ui_EditItemReprInEnvWindow(object):
    def setupUi(self, EditItemReprInEnvWindow):
        EditItemReprInEnvWindow.setObjectName("EditItemReprInEnvWindow")
        EditItemReprInEnvWindow.resize(513, 631)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditItemReprInEnvWindow.sizePolicy().hasHeightForWidth())
        EditItemReprInEnvWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(EditItemReprInEnvWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 96, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(390, 130, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName("editBtn")
        self.TypesComboBox = QtWidgets.QComboBox(self.centralwidget)
        # self.TypesComboBox.setGeometry(QtCore.QRect(170, 310, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TypesComboBox.setFont(font)
        self.TypesComboBox.setObjectName("TypesComboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 420, 311, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.CatComboBox = QtWidgets.QComboBox(self.centralwidget)
        # self.CatComboBox.setGeometry(QtCore.QRect(170, 260, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CatComboBox.setFont(font)
        self.CatComboBox.setObjectName("CatComboBox")
        self.DomComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DomComboBox.setGeometry(QtCore.QRect(170, 210, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DomComboBox.setFont(font)
        self.DomComboBox.setObjectName("DomComboBox")
        self.AttrComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.AttrComboBox.setGeometry(QtCore.QRect(170, 360, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AttrComboBox.setFont(font)
        self.AttrComboBox.setObjectName("AttrComboBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(140, 510, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(20, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(20, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        EditItemReprInEnvWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditItemReprInEnvWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        EditItemReprInEnvWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EditItemReprInEnvWindow)
        self.statusbar.setObjectName("statusbar")
        EditItemReprInEnvWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(EditItemReprInEnvWindow)
        QtCore.QMetaObject.connectSlotsByName(EditItemReprInEnvWindow)

        self.version_id = QtWidgets.QLabel(self.centralwidget)
        self.version_id.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.version_id.setObjectName("version_id")


        self.editBtn.clicked.connect(self.startNow)
        self.saveBtn.clicked.connect(self.saveItem)
        self.saveBtn.clicked.connect(EditItemReprInEnvWindow.close)


    def saveItem(self):
        version_id = int(self.version_id.text())
        cur_dom = str(self.DomComboBox.currentText())
        if str(self.item) == "facts":
            cur_value = str(self.CatComboBox.currentText()) + " " + str(self.TypesComboBox.currentText()) + " " + str(self.AttrComboBox.currentText())
        else:
            cur_value = str(self.TypesComboBox.currentText()) + " " + str(self.CatComboBox.currentText()) + " " + str(self.AttrComboBox.currentText()) + "?"

        cur_time = int(self.lineEdit.text())
        db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
        with closing(db.cursor()) as cur:
            
            cur.execute("UPDATE environment SET domain = '%s', value = '%s', persist_time = '%i', categories = '%s', types = '%s', attributes = '%s' WHERE version_id = '%i' AND domain = '%s' AND value = '%s'"
                                                 % (cur_dom, cur_value, cur_time, ''.join(self.CatComboBox.currentText()), ''.join(self.TypesComboBox.currentText()),
                                                 ''.join(self.AttrComboBox.currentText()), version_id, ''.join(self.origin_dom), ''.join(self.origin_value)))
 
            db.commit()
            QtWidgets.QMessageBox.about(self.centralwidget,'Connection', 'Data Edited Successfully')

    def startNow(self):
        self.DomComboBox.clear()
        self.CatComboBox.clear()
        self.TypesComboBox.clear()
        self.AttrComboBox.clear()
        cur_dom = self.origin_dom
        version_id = int(self.version_id.text())
        db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
        with closing(db.cursor()) as cur:
            cur.execute("SELECT * FROM domains WHERE version_id = '%i'" % (version_id))
            domains = cur.fetchall()
            for x in domains:
                self.DomComboBox.addItem(x[2])
            cur.execute("SELECT * FROM categories WHERE version_id = '%i'" % (version_id))
            categories = cur.fetchall()
            for x in categories:
                self.CatComboBox.addItem(x[2])
            cur.execute("SELECT * FROM types WHERE version_id = '%i'" % (version_id))
            types = cur.fetchall()
            for x in types:
                self.TypesComboBox.addItem(x[2])
            cur.execute("SELECT * FROM attributes WHERE version_id = '%i'" % (version_id))
            attributes = cur.fetchall()
            for x in attributes:
                self.AttrComboBox.addItem(x[2])

        with closing(db.cursor()) as cur:
            cur.execute("SELECT * FROM %s WHERE version_id = '%i' AND value = '%s'" % (str(self.item), version_id, ''.join(self.origin_value)))
            items = cur.fetchall()
            for x in items:
                if str(self.item) == "facts":
                    self.CatComboBox.setCurrentText(x[3])
                    self.TypesComboBox.setCurrentText(x[4])
                    self.AttrComboBox.setCurrentText(x[5])
                else:
                    self.CatComboBox.setCurrentText(x[4])
                    self.TypesComboBox.setCurrentText(x[3])
                    self.AttrComboBox.setCurrentText(x[5])

        self.DomComboBox.setCurrentText(cur_dom)
        # self.CatComboBox.setCurrentText(cur_cat)
        # self.TypesComboBox.setCurrentText(cur_type)
        # self.AttrComboBox.setCurrentText(cur_attr)

    def retranslateUi(self, EditItemReprInEnvWindow):
        _translate = QtCore.QCoreApplication.translate
        EditItemReprInEnvWindow.setWindowTitle(_translate("EditItemReprInEnvWindow", "MainWindow"))
        self.label.setText(_translate("EditItemReprInEnvWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Edit</span></p></body></html>"))
        self.label_2.setText(_translate("EditItemReprInEnvWindow", "Current fact representation"))
        self.label_3.setText(_translate("EditItemReprInEnvWindow", "Animals - Animal can breath - 1 sec"))
        self.editBtn.setText(_translate("EditItemReprInEnvWindow", "Edit"))
        self.label_8.setText(_translate("EditItemReprInEnvWindow", "Retrieval time"))
        self.saveBtn.setText(_translate("EditItemReprInEnvWindow", "Save"))
        self.label_4.setText(_translate("EditItemReprInEnvWindow", "Domain"))
        self.label_5.setText(_translate("EditItemReprInEnvWindow", "Category"))
        self.label_6.setText(_translate("EditItemReprInEnvWindow", "Type"))
        self.label_7.setText(_translate("EditItemReprInEnvWindow", "Attribute"))
        self.menuInteractive_System_Modelling.setTitle(_translate("EditItemReprInEnvWindow", "1"))

