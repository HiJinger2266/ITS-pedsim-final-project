from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow
from views.signal_editor import SignalEditor
from model.enums import FileState
from model.main_model import MainModel
from controllers.main_ctrl import MainController
import qdarkstyle
import tempfile

class MainView(QMainWindow):
    def __init__(self, model: MainModel, main_controller: MainController):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._signal_editor = SignalEditor(self._model, self._main_controller)

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

        ## set initial state
        self._ui.action_close.setEnabled(False)
        self._ui.actio_save.setEnabled(False)
        self._ui.action_edit_signal.setEnabled(False)
        self._ui.action_edit_agents.setEnabled(False)
        self._ui.action_edit_simulation.setEnabled(False)
        self._ui.menuEdit_Geometry.setEnabled(False)
        self._ui.action_reload.setEnabled(False)

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
            self._ui.actio_save.setEnabled(True)
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
            self._ui.actio_save.setEnabled(True)
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
            self._ui.actio_save.setEnabled(True)
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
            self._ui.actio_save.setEnabled(False)
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
        else:
            palette = qdarkstyle.Palette()
            palette.ID = "light"
            self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))

    def _edit_signal(self):
        self._signal_editor.show()