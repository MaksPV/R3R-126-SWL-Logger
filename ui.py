# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled11.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.callsignEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.callsignEdit_1.setFont(font)
        self.callsignEdit_1.setObjectName("callsignEdit_1")
        self.gridLayout.addWidget(self.callsignEdit_1, 3, 0, 1, 2)
        self.hamQTHBox = QtWidgets.QCheckBox(self.centralwidget)
        self.hamQTHBox.setEnabled(True)
        self.hamQTHBox.setChecked(False)
        self.hamQTHBox.setObjectName("hamQTHBox")
        self.gridLayout.addWidget(self.hamQTHBox, 8, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 7, 0, 1, 3)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table.setFont(font)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setRowCount(0)
        self.table.setObjectName("table")
        self.table.setColumnCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(11, item)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(40)
        self.table.horizontalHeader().setMinimumSectionSize(20)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.table, 0, 0, 1, 6)
        self.QTHEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QTHEdit_1.setFont(font)
        self.QTHEdit_1.setText("")
        self.QTHEdit_1.setObjectName("QTHEdit_1")
        self.gridLayout.addWidget(self.QTHEdit_1, 5, 0, 1, 2)
        self.locatorEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locatorEdit_1.setFont(font)
        self.locatorEdit_1.setText("")
        self.locatorEdit_1.setObjectName("locatorEdit_1")
        self.gridLayout.addWidget(self.locatorEdit_1, 5, 2, 1, 1)
        self.realTimeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.realTimeCheckBox.setEnabled(True)
        self.realTimeCheckBox.setChecked(True)
        self.realTimeCheckBox.setTristate(False)
        self.realTimeCheckBox.setObjectName("realTimeCheckBox")
        self.gridLayout.addWidget(self.realTimeCheckBox, 1, 3, 1, 1)
        self.startTimeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.gridLayout.addWidget(self.startTimeEdit, 1, 1, 1, 1)
        self.QTHEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QTHEdit_2.setFont(font)
        self.QTHEdit_2.setText("")
        self.QTHEdit_2.setObjectName("QTHEdit_2")
        self.gridLayout.addWidget(self.QTHEdit_2, 5, 3, 1, 2)
        self.nameEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameEdit_1.setFont(font)
        self.nameEdit_1.setObjectName("nameEdit_1")
        self.gridLayout.addWidget(self.nameEdit_1, 4, 0, 1, 3)
        self.callsignEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.callsignEdit_2.setFont(font)
        self.callsignEdit_2.setObjectName("callsignEdit_2")
        self.gridLayout.addWidget(self.callsignEdit_2, 3, 3, 1, 2)
        self.RSTEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.RSTEdit_2.setFont(font)
        self.RSTEdit_2.setMaxLength(3)
        self.RSTEdit_2.setObjectName("RSTEdit_2")
        self.gridLayout.addWidget(self.RSTEdit_2, 3, 5, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 8, 3, 1, 1)
        self.modeBox = QtWidgets.QComboBox(self.centralwidget)
        self.modeBox.setObjectName("modeBox")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.gridLayout.addWidget(self.modeBox, 1, 4, 1, 1)
        self.commentEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commentEdit_2.setFont(font)
        self.commentEdit_2.setObjectName("commentEdit_2")
        self.gridLayout.addWidget(self.commentEdit_2, 6, 3, 1, 3)
        self.RSTEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.RSTEdit_1.setFont(font)
        self.RSTEdit_1.setMaxLength(3)
        self.RSTEdit_1.setObjectName("RSTEdit_1")
        self.gridLayout.addWidget(self.RSTEdit_1, 3, 2, 1, 1)
        self.beeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.beeEdit.setReadOnly(True)
        self.beeEdit.setObjectName("beeEdit")
        self.gridLayout.addWidget(self.beeEdit, 8, 2, 1, 1)
        self.freqBox = QtWidgets.QSpinBox(self.centralwidget)
        self.freqBox.setMaximum(500000)
        self.freqBox.setProperty("value", 7000)
        self.freqBox.setObjectName("freqBox")
        self.gridLayout.addWidget(self.freqBox, 1, 5, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 7, 3, 1, 3)
        self.commentEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commentEdit_1.setFont(font)
        self.commentEdit_1.setObjectName("commentEdit_1")
        self.gridLayout.addWidget(self.commentEdit_1, 6, 0, 1, 3)
        self.locatorEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locatorEdit_2.setFont(font)
        self.locatorEdit_2.setText("")
        self.locatorEdit_2.setObjectName("locatorEdit_2")
        self.gridLayout.addWidget(self.locatorEdit_2, 5, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 1, 1, 1)
        self.nonClearButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nonClearButton_2.setFont(font)
        self.nonClearButton_2.setCheckable(True)
        self.nonClearButton_2.setChecked(False)
        self.nonClearButton_2.setObjectName("nonClearButton_2")
        self.gridLayout.addWidget(self.nonClearButton_2, 2, 3, 1, 3)
        self.nameEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameEdit_2.setFont(font)
        self.nameEdit_2.setObjectName("nameEdit_2")
        self.gridLayout.addWidget(self.nameEdit_2, 4, 3, 1, 3)
        self.nonClearButton_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nonClearButton_1.setFont(font)
        self.nonClearButton_1.setCheckable(True)
        self.nonClearButton_1.setObjectName("nonClearButton_1")
        self.gridLayout.addWidget(self.nonClearButton_1, 2, 0, 1, 3)
        self.endTimeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.gridLayout.addWidget(self.endTimeEdit, 1, 2, 1, 1)
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 8, 4, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionADIF = QtWidgets.QAction(MainWindow)
        self.actionADIF.setObjectName("actionADIF")
        self.action_from_CSV = QtWidgets.QAction(MainWindow)
        self.action_from_CSV.setObjectName("action_from_CSV")
        self.action_to_CSV = QtWidgets.QAction(MainWindow)
        self.action_to_CSV.setObjectName("action_to_CSV")
        self.actionChangeBand = QtWidgets.QAction(MainWindow)
        self.actionChangeBand.setObjectName("actionChangeBand")
        self.actionChangeMode = QtWidgets.QAction(MainWindow)
        self.actionChangeMode.setObjectName("actionChangeMode")
        self.actionClearBase = QtWidgets.QAction(MainWindow)
        self.actionClearBase.setObjectName("actionClearBase")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.action_eQSL = QtWidgets.QAction(MainWindow)
        self.action_eQSL.setObjectName("action_eQSL")
        self.menu.addAction(self.actionADIF)
        self.menu.addAction(self.action_eQSL)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClearBase)
        self.menu_2.addAction(self.actionChangeBand)
        self.menu_2.addAction(self.actionChangeMode)
        self.menu_3.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "R3R-126 SWL Logger"))
        self.callsignEdit_1.setPlaceholderText(_translate("MainWindow", "CALLSIGN"))
        self.hamQTHBox.setText(_translate("MainWindow", "HamQTH"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time1"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time2"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Freq"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Mode"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Call1"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Call2"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "RST1"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "RST2"))
        item = self.table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Comment1"))
        item = self.table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Comment2"))
        self.QTHEdit_1.setPlaceholderText(_translate("MainWindow", "QTH"))
        self.locatorEdit_1.setPlaceholderText(_translate("MainWindow", "LOCATOR"))
        self.realTimeCheckBox.setText(_translate("MainWindow", "Real Time"))
        self.startTimeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.QTHEdit_2.setPlaceholderText(_translate("MainWindow", "QTH"))
        self.nameEdit_1.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.callsignEdit_2.setPlaceholderText(_translate("MainWindow", "CALLSIGN"))
        self.RSTEdit_2.setPlaceholderText(_translate("MainWindow", "RST"))
        self.clearButton.setText(_translate("MainWindow", "??????????????"))
        self.modeBox.setItemText(0, _translate("MainWindow", "SSB"))
        self.modeBox.setItemText(1, _translate("MainWindow", "CW"))
        self.modeBox.setItemText(2, _translate("MainWindow", "RTTY"))
        self.modeBox.setItemText(3, _translate("MainWindow", "FM"))
        self.modeBox.setItemText(4, _translate("MainWindow", "AM"))
        self.modeBox.setItemText(5, _translate("MainWindow", "DIGI"))
        self.modeBox.setItemText(6, _translate("MainWindow", "Other"))
        self.modeBox.setItemText(7, _translate("MainWindow", "SSTV"))
        self.commentEdit_2.setPlaceholderText(_translate("MainWindow", "COMMENT"))
        self.RSTEdit_1.setPlaceholderText(_translate("MainWindow", "RST"))
        self.commentEdit_1.setPlaceholderText(_translate("MainWindow", "COMMENT"))
        self.locatorEdit_2.setPlaceholderText(_translate("MainWindow", "LOCATOR"))
        self.label.setText(_translate("MainWindow", "??????????:"))
        self.nonClearButton_2.setText(_translate("MainWindow", "???? ??????????????"))
        self.nameEdit_2.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.nonClearButton_1.setText(_translate("MainWindow", "???? ??????????????"))
        self.endTimeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.menu.setTitle(_translate("MainWindow", "????????"))
        self.menu_2.setTitle(_translate("MainWindow", "????????????"))
        self.menu_3.setTitle(_translate("MainWindow", "?? ??????????????????"))
        self.actionADIF.setText(_translate("MainWindow", "?????????????? ?? ADIF"))
        self.actionADIF.setShortcut(_translate("MainWindow", "Alt+A"))
        self.action_from_CSV.setText(_translate("MainWindow", "?????????????? CSV"))
        self.action_from_CSV.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_to_CSV.setText(_translate("MainWindow", "?????????????????? CSV"))
        self.action_to_CSV.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionChangeBand.setText(_translate("MainWindow", "?????????????? ????????????????"))
        self.actionChangeBand.setShortcut(_translate("MainWindow", "Alt+B"))
        self.actionChangeMode.setText(_translate("MainWindow", "?????????????? ??????????"))
        self.actionChangeMode.setShortcut(_translate("MainWindow", "Alt+M"))
        self.actionClearBase.setText(_translate("MainWindow", "???????????????? ??????????????"))
        self.actionAbout.setText(_translate("MainWindow", "????????????????????"))
        self.action_eQSL.setText(_translate("MainWindow", "?????????????? ???? eQSL"))
        self.action_eQSL.setShortcut(_translate("MainWindow", "Alt+E"))
