from PyQt5.QtCore import QObject, pyqtSlot, QSettings, QDateTime
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from model.enums import FileState
from model.main_model import MainModel
import os

class MainController(QObject):
    def __init__(self, model: MainModel):
        super().__init__()

        self._model = model
        self._settings = QSettings('NTU', 'PedSim')

    @pyqtSlot(bool)
    def open_simulation_file(self, value):
        """
        connect with main_view action_open_triggered
        """
        # validate file path
        if not os.path.isfile(value):
            raise FileNotFoundError(f'File not found: {value}')
        # set simulation file path
        self._model.simulation_file = value
        # set simulation file status
        self._model.simulation_file_status = FileState.UNCHANGED

    @pyqtSlot(bool)
    def open_temp_simulation_file(self, value):
        """
        connect with main_view action_open_temp_triggered
        """
        # validate file path
        if not os.path.isfile(value):
            raise FileNotFoundError(f'File not found: {value}')
        # set simulation file path
        self._model.simulation_file = value
        # set simulation file status
        self._model.simulation_file_status = FileState.NEW
        self.set_boundaries([])
        self.set_origins([])
        self.set_destinations([])

    @pyqtSlot(bool)
    def save_simulation_file(self):
        """
        connect with main_view action_save_triggered
        """
        # validate file path
        if not os.path.isfile(self._model.simulation_file):
            raise FileNotFoundError(f'File not found: {self._model.simulation_file}')
        if self._model.simulation_file_status == FileState.NEW:
            # ask for new file path
            file_path, _ = QFileDialog.getSaveFileName(None, 'Save Simulation File', '', 'Simulation Files (*.sim);;All Files (*)')
            # validate file path
            if file_path:
                with open(file_path, 'w') as f:
                    f.write(QDateTime.currentDateTime().toString())
            else:
                return
            # set simulation file path
            self._model.simulation_file = file_path
            # set simulation file status
        # TODO: save simulation file
        pass
        self._model.simulation_file_status = FileState.UNCHANGED
        

    @pyqtSlot(bool)
    def toggle_dark_mode(self, value):
        self._model.dark_mode = not self._model.dark_mode
        self._settings.setValue('dark_mode', self._model.dark_mode)


    @pyqtSlot(bool)
    def set_cursor_mode(self, value):
        self._model.cursor_mode = value

    @pyqtSlot(bool)
    def set_statusBar_message(self, value):
        self._model.statusBar_message = value

    @pyqtSlot(bool)
    def set_boundaries(self, value):
        self._model.boundaries = value

    @pyqtSlot(bool)
    def set_origins(self, value):
        self._model.origins = value

    @pyqtSlot(bool)
    def set_destinations(self, value):
        self._model.destinations = value

    @pyqtSlot(bool)
    def set_background(self, value):
        self._model.background = value