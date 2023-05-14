from PyQt5.QtCore import QObject, pyqtSignal
import os

class MainModel(QObject):

    gemoetry_file_changed = pyqtSignal(str)
    simulation_file_changed = pyqtSignal(str)
    dark_mode_changed = pyqtSignal(bool)

    @property
    def geometry_file(self):
        return self._geometry_file
    
    @geometry_file.setter
    def geometry_file(self, value):
        if not os.path.isfile(value):
            raise FileNotFoundError(f'File not found: {value}')
        self._geometry_file = value
        self.gemoetry_file_changed.emit(value)

    @property
    def simulation_file(self):
        return self._simulation_file
    
    @simulation_file.setter
    def simulation_file(self, value):
        if not os.path.isfile(value):
            raise FileNotFoundError(f'File not found: {value}')
        self._simulation_file = value
        self.simulation_file_changed.emit(value)

    @property
    def dark_mode(self):
        return self._dark_mode
    
    @dark_mode.setter
    def dark_mode(self, value):
        self._dark_mode = value
        self.dark_mode_changed.emit(value)

    def __init__(self):
        super().__init__()
        self._geometry_file = None
        self._simulation_file = None
        self._dark_mode = False