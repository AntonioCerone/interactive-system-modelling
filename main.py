# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
import MySQLdb as mdb

from create_project import Ui_EditProjectInfoWindow
from create_version import Ui_EditVersionInfoWindow
from project_desc import Ui_ProjectDescWindow
from version_desc import Ui_VersionDescWindow
from project import Ui_ProjectWindow

db = mdb.connect('127.0.0.1', 'root', '', 'interSys')

projects_dict = {}

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1162, 861)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createBtn.setGeometry(QtCore.QRect(850, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.createBtn.setFont(font)
        self.createBtn.setObjectName("createBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 591, 51))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 80, 121, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 80, 151, 51))
        self.label_3.setObjectName("label_3")
        self.editProjInfoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editProjInfoBtn.setGeometry(QtCore.QRect(170, 350, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editProjInfoBtn.setFont(font)
        self.editProjInfoBtn.setObjectName("editProjInfoBtn")
        self.deleteProjBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteProjBtn.setGeometry(QtCore.QRect(330, 350, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteProjBtn.setFont(font)
        self.deleteProjBtn.setObjectName("deleteProjBtn")
        self.editVerInfoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editVerInfoBtn.setGeometry(QtCore.QRect(690, 350, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editVerInfoBtn.setFont(font)
        self.editVerInfoBtn.setObjectName("editVerInfoBtn")
        self.deleteVerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteVerBtn.setGeometry(QtCore.QRect(850, 350, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteVerBtn.setFont(font)
        self.deleteVerBtn.setObjectName("deleteVerBtn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(110, 130, 381, 261))
        self.listWidget.setObjectName("listWidget")
        # item = QtWidgets.QListWidgetItem()
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # item.setFont(font)
        # self.listWidget.addItem(item)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(630, 130, 381, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setItem(1, 1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(182)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 420, 301, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 420, 311, 51))
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 480, 381, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(630, 480, 381, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.viewProjDescBtn = QtWidgets.QPushButton(self.centralwidget)
        self.viewProjDescBtn.setGeometry(QtCore.QRect(180, 710, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.viewProjDescBtn.setFont(font)
        self.viewProjDescBtn.setObjectName("viewProjDescBtn")
        self.viewVerDescBtn = QtWidgets.QPushButton(self.centralwidget)
        self.viewVerDescBtn.setGeometry(QtCore.QRect(700, 710, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.viewVerDescBtn.setFont(font)
        self.viewVerDescBtn.setObjectName("viewVerDescBtn")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(988, 744, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.openBtn.setFont(font)
        self.openBtn.setObjectName("openBtn")
        self.tableWidget.raise_()
        self.listWidget.raise_()
        self.createBtn.raise_()
        self.label.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.editProjInfoBtn.raise_()
        self.deleteProjBtn.raise_()
        self.editVerInfoBtn.raise_()
        self.deleteVerBtn.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.viewProjDescBtn.raise_()
        self.viewVerDescBtn.raise_()
        self.openBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1162, 22))
        self.menubar.setObjectName("menubar")
        self.menuInteractive_System_Modelling = QtWidgets.QMenu(self.menubar)
        self.menuInteractive_System_Modelling.setObjectName("menuInteractive_System_Modelling")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInteractive_System_Modelling.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.createBtn.clicked.connect(self.new_project)
        self.editProjInfoBtn.clicked.connect(self.edit_project)
        self.editVerInfoBtn.clicked.connect(self.edit_version)
        self.viewProjDescBtn.clicked.connect(self.project_desc)
        self.viewVerDescBtn.clicked.connect(self.version_desc)
        self.deleteProjBtn.clicked.connect(self.delete_project)
        self.deleteVerBtn.clicked.connect(self.delete_version)
        self.openBtn.clicked.connect(self.open_project)
        self.listWidget.itemClicked.connect(self.show_short_descr)
        self.get_projects()

    def show_short_descr(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return  
        for item in listItems:
            self.textBrowser.clear()
            self.textBrowser.append(projects_dict[item.text()][0])


    def get_projects(self):
        with db:
            cur = db.cursor()
            cur.execute("SELECT * FROM projects")
            projects = cur.fetchall()

            for x in projects:
                self.listWidget.addItem(x[1])
                projects_dict[x[1]] = [x[2], x[3]]


    def delete_project(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return   
        reply = QMessageBox.question(self, "Delete project", "Are you sure you want to delete this project and its versions?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            for item in listItems:
                self.listWidget.takeItem(self.listWidget.row(item))
                db = mdb.connect('127.0.0.1', 'root', '', 'interSys')
                with db:
                    cur = db.cursor()
                    cur.execute("DELETE FROM projects WHERE name = '%s'" % (''.join(item.text())))
                    db.commit()

        else:
            return

    def delete_version(self):
        tableItems=self.tableWidget.selectedItems()
        if not tableItems: return   
        reply = QMessageBox.question(self, "Delete version", "Are you sure you want to delete this version?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            for item in tableItems:
               self.tableWidget.takeItem(self.tableWidget.row(item), self.tableWidget.column(item))
        else:
            return

    def new_project(self):
        self.EditProjectInfoWindow = QtWidgets.QMainWindow()
        self.ui = Ui_EditProjectInfoWindow()
        self.ui.setupUi(self.EditProjectInfoWindow)
        self.EditProjectInfoWindow.show()

    def edit_project(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return  
        for item in listItems:
            self.EditProjectInfoWindow = QtWidgets.QMainWindow()
            self.ui = Ui_EditProjectInfoWindow()
            self.ui.setupUi(self.EditProjectInfoWindow)
            self.EditProjectInfoWindow.show()

    def edit_version(self):
        tableItems=self.tableWidget.selectedItems()
        if not tableItems: return  
        for item in tableItems:
            self.EditVersionInfoWindow = QtWidgets.QMainWindow()
            self.ui = Ui_EditVersionInfoWindow()
            self.ui.setupUi(self.EditVersionInfoWindow)
            self.EditVersionInfoWindow.show()

    def project_desc(self):
        self.ProjectDescWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ProjectDescWindow()
        self.ui.setupUi(self.ProjectDescWindow)
        self.ProjectDescWindow.show()

    def version_desc(self):
        self.VersionDescWindow = QtWidgets.QMainWindow()
        self.ui = Ui_VersionDescWindow()
        self.ui.setupUi(self.VersionDescWindow)
        self.VersionDescWindow.show()

    def open_project(self):
        listItems=self.listWidget.selectedItems()
        tableItems=self.tableWidget.selectedItems()
        if not listItems: return 
        if not tableItems: return 
        self.ProjectWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ProjectWindow()
        self.ui.setupUi(self.ProjectWindow)
        self.ProjectWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createBtn.setText(_translate("MainWindow", "Create a Project"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">Interactive System Modelling</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Projects</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Versions</span></p></body></html>"))
        self.editProjInfoBtn.setText(_translate("MainWindow", "Edit Info"))
        self.deleteProjBtn.setText(_translate("MainWindow", "Delete"))
        self.editVerInfoBtn.setText(_translate("MainWindow", "Edit Info"))
        self.deleteVerBtn.setText(_translate("MainWindow", "Delete"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        # item = self.listWidget.item(0)
        # item.setText(_translate("MainWindow", "Animal-Dog"))


        self.listWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Version #"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Version Name 1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "1.0"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Version Name 2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "1.1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Project Description</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Version Description</span></p></body></html>"))
#         self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">This project blablaballabalbaalalalabalalbalablabal</span></p></body></html>"))
#         self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">This version blablaballabalbaalalalabalalbalablabal</span></p></body></html>"))
        self.viewProjDescBtn.setText(_translate("MainWindow", "View Long Description"))
        self.viewVerDescBtn.setText(_translate("MainWindow", "View Long Description"))
        self.openBtn.setText(_translate("MainWindow", "Open"))
        self.menuInteractive_System_Modelling.setTitle(_translate("MainWindow", "1"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
    
