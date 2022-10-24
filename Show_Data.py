# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Show_Data.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 770)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/suurennuslasi.png.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("/* set background color for mainwindow */\n"
"#MainWindow {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.00568182, x2:1, y2:0, stop:0 rgba(54, 160, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"/* set style for QGroupBox in mainwindow */\n"
"#MainWindow QGroupBox {\n"
"    border: 1px solid #c6c6c6;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* set style for title QGroupBox */\n"
"#groupBox {\n"
"    border: None;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.00568182, x2:1, y2:0, stop:0 rgba(54, 160, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"/* set style for result QGroupBox */\n"
"#groupBox_2 {\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* set style for all the QPushButton in mainwindow */\n"
"#MainWindow QPushButton {\n"
"    border-radius: 5px;\n"
"    border:1px solid rgb(127, 127, 127);\n"
"    background-color: #fff;\n"
"    padding: 4px 8px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#MainWindow QPushButton:hover {\n"
"    background-color: #00aaff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#MainWindow QPushButton:pressed {\n"
"    padding-left: 15px;\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/suurennuslasi1.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(496, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(917, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(203, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.get_path_btn = QtWidgets.QPushButton(self.widget)
        self.get_path_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.get_path_btn.setMaximumSize(QtCore.QSize(1000, 1000))
        self.get_path_btn.setObjectName("get_path_btn")
        self.horizontalLayout_2.addWidget(self.get_path_btn)
        self.save_btn = QtWidgets.QPushButton(self.widget)
        self.save_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.get_data_btn = QtWidgets.QPushButton(self.widget)
        self.get_data_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.get_data_btn.setObjectName("get_data_btn")
        self.horizontalLayout_2.addWidget(self.get_data_btn)
        spacerItem2 = QtWidgets.QSpacerItem(105, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignVCenter)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show Data"))
        self.label_2.setText(_translate("MainWindow", "Get and Show Data from MySQL Database"))
        self.get_path_btn.setText(_translate("MainWindow", "Save Path"))
        self.save_btn.setText(_translate("MainWindow", "Save Data"))
        self.get_data_btn.setText(_translate("MainWindow", "Get Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Column 1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Column 2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Column 3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Column 4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Column 5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Column 6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Column 7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Column 8"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Column 9"))
import resource_rc
