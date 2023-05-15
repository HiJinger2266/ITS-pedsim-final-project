# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/img/app_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 190, 411, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Simulation = QtWidgets.QAction(MainWindow)
        self.actionOpen_Simulation.setObjectName("actionOpen_Simulation")
        self.actionOpen_Geometry = QtWidgets.QAction(MainWindow)
        self.actionOpen_Geometry.setObjectName("actionOpen_Geometry")
        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionEdit_Road = QtWidgets.QAction(MainWindow)
        self.actionEdit_Road.setObjectName("actionEdit_Road")
        self.actionEdit_Ped = QtWidgets.QAction(MainWindow)
        self.actionEdit_Ped.setObjectName("actionEdit_Ped")
        self.actionEdit_Ped_Crossing = QtWidgets.QAction(MainWindow)
        self.actionEdit_Ped_Crossing.setObjectName("actionEdit_Ped_Crossing")
        self.actionEdit_Sep_Island = QtWidgets.QAction(MainWindow)
        self.actionEdit_Sep_Island.setObjectName("actionEdit_Sep_Island")
        self.actionToggle_Dark_Mode = QtWidgets.QAction(MainWindow)
        self.actionToggle_Dark_Mode.setObjectName("actionToggle_Dark_Mode")
        self.actionSave_Simulation = QtWidgets.QAction(MainWindow)
        self.actionSave_Simulation.setObjectName("actionSave_Simulation")
        self.actionSave_Geometry = QtWidgets.QAction(MainWindow)
        self.actionSave_Geometry.setObjectName("actionSave_Geometry")
        self.menuFile.addAction(self.actionOpen_Simulation)
        self.menuFile.addAction(self.actionOpen_Geometry)
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave_Simulation)
        self.menuFile.addAction(self.actionSave_Geometry)
        self.menuSetting.addAction(self.actionToggle_Dark_Mode)
        self.menuEdit.addAction(self.actionEdit)
        self.menuEdit.addAction(self.actionEdit_Road)
        self.menuEdit.addAction(self.actionEdit_Ped)
        self.menuEdit.addAction(self.actionEdit_Ped_Crossing)
        self.menuEdit.addAction(self.actionEdit_Sep_Island)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PedSim"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen_Simulation.setText(_translate("MainWindow", "Open Simulation"))
        self.actionOpen_Geometry.setText(_translate("MainWindow", "Open Geometry"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionEdit.setText(_translate("MainWindow", "Edit Signal"))
        self.actionEdit_Road.setText(_translate("MainWindow", "Edit Road"))
        self.actionEdit_Ped.setText(_translate("MainWindow", "Edit Bike Lane"))
        self.actionEdit_Ped_Crossing.setText(_translate("MainWindow", "Edit Ped Crossing"))
        self.actionEdit_Sep_Island.setText(_translate("MainWindow", "Edit Sep Island"))
        self.actionToggle_Dark_Mode.setText(_translate("MainWindow", "Toggle Dark Mode"))
        self.actionSave_Simulation.setText(_translate("MainWindow", "Save Simulation"))
        self.actionSave_Geometry.setText(_translate("MainWindow", "Save Geometry"))
import resource_rc
