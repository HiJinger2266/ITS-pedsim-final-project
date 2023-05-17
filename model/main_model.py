from PyQt5.QtCore import QObject, pyqtSignal
from model.enums import FileState

class MainModel(QObject):
    """
    contains the data of the application:
    - simulation_file_path: path to the simulation file
    - dark_mode: True if dark mode is enabled
    """
    simulation_file_path_changed = pyqtSignal(str)
    simulation_file_status_changed = pyqtSignal(FileState)
    dark_mode_changed = pyqtSignal(bool)

    @property
    def simulation_file_path(self):
        return self._simulation_file_path
    
    @simulation_file_path.setter
    def simulation_file_path(self, value):
        self._simulation_file_path = value
        self.simulation_file_path_changed.emit(value)

    @property
    def dark_mode(self):
        return self._dark_mode
    
    @dark_mode.setter
    def dark_mode(self, value):
        self._dark_mode = value
        self.dark_mode_changed.emit(value)

    @property
    def simulation_file_status(self):
        return self._simulation_file_status
    
    @simulation_file_status.setter
    def simulation_file_status(self, value):
        self._simulation_file_status = value
        self.simulation_file_status_changed.emit(value)

    def __init__(self):
        super().__init__()
        self._geometry_file = None
        self._simulation_file_path = ''
        self._dark_mode = False
