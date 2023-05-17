from PyQt5.QtCore import QObject, pyqtSlot, QSettings
from model.enums import FileState
import os

class MainController(QObject):
    def __init__(self, model):
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

    @pyqtSlot(bool)
    def toggle_dark_mode(self, value):
        self._model.dark_mode = not self._model.dark_mode
        self._settings.setValue('dark_mode', self._model.dark_mode)
