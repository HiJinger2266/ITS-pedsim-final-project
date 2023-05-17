from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot, QSettings, Qt
from PyQt5.QtGui import QCursor
from views.main_view_ui import Ui_MainWindow
from views.signal_editor import SignalEditor
from views.agents_editor import AgentsEditor
from model.enums import FileState, CursorMode
from model.main_model import MainModel
from controllers.main_ctrl import MainController
import qdarkstyle
import tempfile
import os, sys

IMG_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'img')

class MainView(QMainWindow):
    def __init__(self, model: MainModel, main_controller: MainController):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        # load settings
        self._settings = QSettings('NTU', 'PedSim')
        # add toolbars
        self._ui.toolBar_file = self.addToolBar("File")
        self._ui.toolBar_edit = self.addToolBar("Edit")
        self._ui.toolBar_view = self.addToolBar("View")
        self._ui.toolBar_settings = self.addToolBar("Settings")
        # add actions to toolbars
        self._ui.toolBar_file.addAction(self._ui.action_open)
        self._ui.toolBar_file.addAction(self._ui.action_save)
        self._ui.toolBar_file.addAction(self._ui.action_close)
        self._ui.toolBar_file.addAction(self._ui.action_reload)
        
        self._ui.toolBar_edit.addAction(self._ui.action_edit_simulation)
        self._ui.toolBar_edit.addAction(self._ui.action_edit_signal)
        self._ui.toolBar_edit.addAction(self._ui.action_edit_agents)

        self._ui.toolBar_view.addAction(self._ui.action_pan)
        self._ui.toolBar_view.addAction(self._ui.action_pointer)
        self._ui.toolBar_view.addAction(self._ui.action_fit)

        self._ui.toolBar_settings.addAction(self._ui.action_toggle_dark_mode)

        self._ui.action_toggle_toolbar_edit.triggered.connect(lambda: self._ui.toolBar_edit.setVisible(self._ui.action_toggle_toolbar_edit.isChecked()))
        self._ui.action_toggle_toolbar_view.triggered.connect(lambda: self._ui.toolBar_view.setVisible(self._ui.action_toggle_toolbar_view.isChecked()))
        self._ui.action_toggle_toolbar_settings.triggered.connect(lambda: self._ui.toolBar_settings.setVisible(self._ui.action_toggle_toolbar_settings.isChecked()))
        self._ui.action_toggle_toolbar_file.triggered.connect(lambda: self._ui.toolBar_file.setVisible(self._ui.action_toggle_toolbar_file.isChecked()))

        self._signal_editor = SignalEditor(self._model, self._main_controller)
        self._agents_editor = AgentsEditor(self._model, self._main_controller)

        # set stylesheet
        palette = qdarkstyle.Palette()
        palette.ID = "light"
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))

        # connect widgets to controller
        self._ui.action_toggle_dark_mode.triggered.connect(self._main_controller.toggle_dark_mode)

        # listen for model event signals
        self._model.simulation_file_path_changed.connect(self.on_simulation_file_path_changed)
        self._model.simulation_file_status_changed.connect(self.on_simulation_file_status_changed)
        self._model.dark_mode_changed.connect(self.on_dark_mode_changed)

        # connect menu items
        self._ui.action_edit_signal.triggered.connect(self._edit_signal)
        self._ui.action_edit_agents.triggered.connect(self._edit_agents)

        ## set initial state
        self._ui.action_close.setEnabled(False)
        self._ui.action_save.setEnabled(False)
        self._ui.action_edit_signal.setEnabled(False)
        self._ui.action_edit_agents.setEnabled(False)
        self._ui.action_edit_simulation.setEnabled(False)
        self._ui.menuEdit_Geometry.setEnabled(False)
        self._ui.action_reload.setEnabled(False)
        
        if self._settings.value('dark_mode', type=bool) is None:
            self._settings.setValue('dark_mode', False)
        # set dark mode
        if self._settings.value('dark_mode', type=bool):
            self._main_controller.toggle_dark_mode(True)

    @pyqtSlot(str)
    def on_simulation_file_path_changed(self, value):
        """
        This slot is called when the simulation_file property of the model changes.
        """
        self._ui.statusbar.showMessage(f'Simulation File Opened: {value}')

    @pyqtSlot(FileState)
    def on_simulation_file_status_changed(self, value):
        """
        This slot is called when the simulation_file_status property of the model changes.
        """
        if value == FileState.UNCHANGED:
            # make actions available
            self._ui.action_close.setEnabled(True)
            self._ui.action_save.setEnabled(True)
            self._ui.action_edit_signal.setEnabled(True)
            self._ui.action_edit_agents.setEnabled(True)
            self._ui.action_edit_simulation.setEnabled(True)
            self._ui.menuEdit_Geometry.setEnabled(True)
            self._ui.action_reload.setEnabled(True)
            # set title
            self.setWindowTitle(f'PedSim - {self._model.simulation_file}')
        elif value == FileState.MODIFIED:
            # make actions available
            self._ui.action_close.setEnabled(True)
            self._ui.action_save.setEnabled(True)
            self._ui.action_edit_signal.setEnabled(True)
            self._ui.action_edit_agents.setEnabled(True)
            self._ui.action_edit_simulation.setEnabled(True)
            self._ui.menuEdit_Geometry.setEnabled(True)
            self._ui.action_reload.setEnabled(True)
            # set title
            self.setWindowTitle(f'PedSim - {self._model.simulation_file} *')

        elif value == FileState.NEW:
            # make actions available
            self._ui.action_close.setEnabled(True)
            self._ui.action_save.setEnabled(True)
            self._ui.action_edit_signal.setEnabled(True)
            self._ui.action_edit_agents.setEnabled(True)
            self._ui.action_edit_simulation.setEnabled(True)
            self._ui.menuEdit_Geometry.setEnabled(True)
            self._ui.action_reload.setEnabled(True)
            # set title
            self.setWindowTitle(f'PedSim - {self._model.simulation_file} *')

        elif value == FileState.CLOSED:
            # make actions unavailable
            self._ui.action_close.setEnabled(False)
            self._ui.action_save.setEnabled(False)
            self._ui.action_edit_signal.setEnabled(False)
            self._ui.action_edit_agents.setEnabled(False)
            self._ui.action_edit_simulation.setEnabled(False)
            self._ui.menuEdit_Geometry.setEnabled(False)
            self._ui.action_reload.setEnabled(False)
            # set title
            self.setWindowTitle(f'PedSim')

    @pyqtSlot()
    def on_action_open_triggered(self):
        """
        This slot is called when the user clicks the Open Simulation menu item.
        """
        # open file dialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Simulation File', '', 'Simulation Files (*.sim);;All Files (*)')
        if file_name:
            self._main_controller.open_simulation_file(file_name)

    @pyqtSlot()
    def on_action_new_triggered(self):
        """
        This slot is called when the user clicks the New Simulation menu item.
        """
        # create temp file at user's temp directory
        temp_folder = tempfile.gettempdir()
        # make delete=True when done debugging
        temp_file = tempfile.NamedTemporaryFile(suffix='.sim', dir=temp_folder, delete=False)
        self._main_controller.open_temp_simulation_file(temp_file.name)

    @pyqtSlot(bool)
    def on_dark_mode_changed(self, value):
        """
        This slot is called when the dark_mode property of the model changes.
        """
        if value:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            # if windows:
            if sys.platform == 'win32':
                # set window title bar color
                from ctypes import windll, byref, sizeof, c_int16, c_int
                from ctypes.wintypes import HWND
                _HWND = self.winId().__int__()
                DWMWA_ATTRIBUTE = 35
                COLOR = 0x002d2319
                windll.dwmapi.DwmSetWindowAttribute(_HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))

        else:
            palette = qdarkstyle.Palette()
            palette.ID = "light"
            self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))
            if sys.platform == 'win32':
                # set window title bar color
                from ctypes import windll, byref, sizeof, c_int16, c_int
                from ctypes.wintypes import HWND
                _HWND = self.winId().__int__()
                DWMWA_ATTRIBUTE = 35
                COLOR = 0x00ffffff
                windll.dwmapi.DwmSetWindowAttribute(_HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
            

    def _edit_signal(self):
        self._signal_editor.show()

    def _edit_agents(self):
        self._agents_editor.show()

    def on_action_pan_triggered(self):
        """
        This slot is called when the user clicks the Pan menu item.
        """
        self._ui.frame.setCursor(Qt.CursorShape.OpenHandCursor)

    def on_action_pointer_triggered(self):
        """
        This slot is called when the user clicks the Pointer menu item.
        """
        self._ui.frame.setCursor(Qt.CursorShape.ArrowCursor)

    def on_action_edit_road_triggered(self):
        """
        This slot is called when the user clicks the Road Edit menu item.
        """
        self._ui.frame.setCursor(Qt.CursorShape.CrossCursor)