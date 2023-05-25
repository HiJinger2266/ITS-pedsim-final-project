# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\ui\main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/img/app_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.canvas = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas.setMouseTracking(True)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuEdit_Geometry = QtWidgets.QMenu(self.menuEdit)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/geometry.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuEdit_Geometry.setIcon(icon1)
        self.menuEdit_Geometry.setObjectName("menuEdit_Geometry")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuToolbars = QtWidgets.QMenu(self.menuView)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/toolbar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuToolbars.setIcon(icon2)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.dockWidgetContents)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.action_open = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open.setIcon(icon3)
        self.action_open.setObjectName("action_open")
        self.actio_open_geometry = QtWidgets.QAction(MainWindow)
        self.actio_open_geometry.setObjectName("actio_open_geometry")
        self.action_reload = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/reload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_reload.setIcon(icon4)
        self.action_reload.setObjectName("action_reload")
        self.action_close = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon5)
        self.action_close.setObjectName("action_close")
        self.action_edit_signal = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/signal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_signal.setIcon(icon6)
        self.action_edit_signal.setObjectName("action_edit_signal")
        self.actionEdit_Road = QtWidgets.QAction(MainWindow)
        self.actionEdit_Road.setObjectName("actionEdit_Road")
        self.actionEdit_Ped = QtWidgets.QAction(MainWindow)
        self.actionEdit_Ped.setObjectName("actionEdit_Ped")
        self.actionEdit_Ped_Crossing = QtWidgets.QAction(MainWindow)
        self.actionEdit_Ped_Crossing.setObjectName("actionEdit_Ped_Crossing")
        self.actionEdit_Sep_Island = QtWidgets.QAction(MainWindow)
        self.actionEdit_Sep_Island.setObjectName("actionEdit_Sep_Island")
        self.action_toggle_dark_mode = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/dark_mode.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_toggle_dark_mode.setIcon(icon7)
        self.action_toggle_dark_mode.setObjectName("action_toggle_dark_mode")
        self.action_save = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon8)
        self.action_save.setObjectName("action_save")
        self.action_save_geometry = QtWidgets.QAction(MainWindow)
        self.action_save_geometry.setObjectName("action_save_geometry")
        self.action_new = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new.setIcon(icon9)
        self.action_new.setObjectName("action_new")
        self.action_edit_agents = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/agent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_agents.setIcon(icon10)
        self.action_edit_agents.setObjectName("action_edit_agents")
        self.action_edit_simulation = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/simulation.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_simulation.setIcon(icon11)
        self.action_edit_simulation.setObjectName("action_edit_simulation")
        self.action_bike_boundary = QtWidgets.QAction(MainWindow)
        self.action_bike_boundary.setObjectName("action_bike_boundary")
        self.action_edit_road = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_road.setIcon(icon12)
        self.action_edit_road.setObjectName("action_edit_road")
        self.action_add_road = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_road.setIcon(icon13)
        self.action_add_road.setObjectName("action_add_road")
        self.action_remove_road = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove_road.setIcon(icon14)
        self.action_remove_road.setObjectName("action_remove_road")
        self.action_edit_bound = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/edit_boundary.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_bound.setIcon(icon15)
        self.action_edit_bound.setObjectName("action_edit_bound")
        self.action_add_bound = QtWidgets.QAction(MainWindow)
        self.action_add_bound.setIcon(icon13)
        self.action_add_bound.setObjectName("action_add_bound")
        self.action_remove_bound = QtWidgets.QAction(MainWindow)
        self.action_remove_bound.setIcon(icon14)
        self.action_remove_bound.setObjectName("action_remove_bound")
        self.action_pan = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/pan.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pan.setIcon(icon16)
        self.action_pan.setObjectName("action_pan")
        self.action_pointer = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/pointer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pointer.setIcon(icon17)
        self.action_pointer.setObjectName("action_pointer")
        self.action_toggle_toolbar_file = QtWidgets.QAction(MainWindow)
        self.action_toggle_toolbar_file.setCheckable(True)
        self.action_toggle_toolbar_file.setChecked(True)
        self.action_toggle_toolbar_file.setObjectName("action_toggle_toolbar_file")
        self.action_toggle_toolbar_edit = QtWidgets.QAction(MainWindow)
        self.action_toggle_toolbar_edit.setCheckable(True)
        self.action_toggle_toolbar_edit.setChecked(True)
        self.action_toggle_toolbar_edit.setObjectName("action_toggle_toolbar_edit")
        self.action_toggle_toolbar_view = QtWidgets.QAction(MainWindow)
        self.action_toggle_toolbar_view.setCheckable(True)
        self.action_toggle_toolbar_view.setChecked(True)
        self.action_toggle_toolbar_view.setObjectName("action_toggle_toolbar_view")
        self.action_toggle_toolbar_settings = QtWidgets.QAction(MainWindow)
        self.action_toggle_toolbar_settings.setCheckable(True)
        self.action_toggle_toolbar_settings.setChecked(True)
        self.action_toggle_toolbar_settings.setObjectName("action_toggle_toolbar_settings")
        self.action_fit = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_fit.setIcon(icon18)
        self.action_fit.setObjectName("action_fit")
        self.action_start = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/start.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_start.setIcon(icon19)
        self.action_start.setObjectName("action_start")
        self.action_pause = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pause.setIcon(icon20)
        self.action_pause.setObjectName("action_pause")
        self.action_stop = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_stop.setIcon(icon21)
        self.action_stop.setObjectName("action_stop")
        self.action_toggle_toolbar_run = QtWidgets.QAction(MainWindow)
        self.action_toggle_toolbar_run.setObjectName("action_toggle_toolbar_run")
        self.action_edit_origin = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/edit_origin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_origin.setIcon(icon22)
        self.action_edit_origin.setObjectName("action_edit_origin")
        self.action_edit_destination = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/edit_destination.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_edit_destination.setIcon(icon23)
        self.action_edit_destination.setObjectName("action_edit_destination")
        self.action_background = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(".\\resources\\ui\\../img/background.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_background.setIcon(icon24)
        self.action_background.setObjectName("action_background")
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_close)
        self.menuFile.addAction(self.action_reload)
        self.menuFile.addAction(self.action_background)
        self.menuSetting.addAction(self.action_toggle_dark_mode)
        self.menuEdit_Geometry.addAction(self.action_edit_bound)
        self.menuEdit_Geometry.addAction(self.action_edit_origin)
        self.menuEdit_Geometry.addAction(self.action_edit_destination)
        self.menuEdit.addAction(self.action_edit_signal)
        self.menuEdit.addAction(self.action_edit_agents)
        self.menuEdit.addAction(self.action_edit_simulation)
        self.menuEdit.addAction(self.menuEdit_Geometry.menuAction())
        self.menuToolbars.addAction(self.action_toggle_toolbar_file)
        self.menuToolbars.addAction(self.action_toggle_toolbar_edit)
        self.menuToolbars.addAction(self.action_toggle_toolbar_view)
        self.menuToolbars.addAction(self.action_toggle_toolbar_settings)
        self.menuToolbars.addAction(self.action_toggle_toolbar_run)
        self.menuView.addAction(self.action_pan)
        self.menuView.addAction(self.action_pointer)
        self.menuView.addAction(self.action_fit)
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuRun.addAction(self.action_start)
        self.menuRun.addAction(self.action_pause)
        self.menuRun.addAction(self.action_stop)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PedSim"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuEdit_Geometry.setTitle(_translate("MainWindow", "Edit Geometry"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuToolbars.setTitle(_translate("MainWindow", "Toolbars"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Objects"))
        self.comboBox.setItemText(0, _translate("MainWindow", "boundaries"))
        self.comboBox.setItemText(1, _translate("MainWindow", "origin"))
        self.comboBox.setItemText(2, _translate("MainWindow", "destination"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.actio_open_geometry.setText(_translate("MainWindow", "Open Geometry"))
        self.action_reload.setText(_translate("MainWindow", "Reload"))
        self.action_close.setText(_translate("MainWindow", "Close"))
        self.action_edit_signal.setText(_translate("MainWindow", "Edit Signal"))
        self.actionEdit_Road.setText(_translate("MainWindow", "Edit Road"))
        self.actionEdit_Ped.setText(_translate("MainWindow", "Edit Bike Lane"))
        self.actionEdit_Ped_Crossing.setText(_translate("MainWindow", "Edit Ped Crossing"))
        self.actionEdit_Sep_Island.setText(_translate("MainWindow", "Edit Sep Island"))
        self.action_toggle_dark_mode.setText(_translate("MainWindow", "Toggle Dark Mode"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save_geometry.setText(_translate("MainWindow", "Save Geometry"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_edit_agents.setText(_translate("MainWindow", "Edit Agents"))
        self.action_edit_simulation.setText(_translate("MainWindow", "Edit Simulation"))
        self.action_bike_boundary.setText(_translate("MainWindow", "Bike Boundary"))
        self.action_edit_road.setText(_translate("MainWindow", "Edit"))
        self.action_add_road.setText(_translate("MainWindow", "Add"))
        self.action_remove_road.setText(_translate("MainWindow", "Remove"))
        self.action_edit_bound.setText(_translate("MainWindow", "Boundary"))
        self.action_add_bound.setText(_translate("MainWindow", "Add"))
        self.action_remove_bound.setText(_translate("MainWindow", "Remove"))
        self.action_pan.setText(_translate("MainWindow", "Pan"))
        self.action_pointer.setText(_translate("MainWindow", "Pointer"))
        self.action_toggle_toolbar_file.setText(_translate("MainWindow", "File"))
        self.action_toggle_toolbar_edit.setText(_translate("MainWindow", "Edit"))
        self.action_toggle_toolbar_view.setText(_translate("MainWindow", "View"))
        self.action_toggle_toolbar_settings.setText(_translate("MainWindow", "Setting"))
        self.action_fit.setText(_translate("MainWindow", "fit"))
        self.action_start.setText(_translate("MainWindow", "Start"))
        self.action_pause.setText(_translate("MainWindow", "Pause"))
        self.action_stop.setText(_translate("MainWindow", "Stop"))
        self.action_toggle_toolbar_run.setText(_translate("MainWindow", "run"))
        self.action_edit_origin.setText(_translate("MainWindow", "Origin"))
        self.action_edit_destination.setText(_translate("MainWindow", "Destination"))
        self.action_background.setText(_translate("MainWindow", "Add Background"))
import resource_rc
