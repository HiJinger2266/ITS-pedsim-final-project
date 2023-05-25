from PyQt5.QtCore import QObject, pyqtSignal
import pandas as pd
import pickle
from model.enums import FileState, CursorMode
from model.table_models import PolygonsTableModel

class MainModel(QObject):
    """
    contains the data of the application:
    - simulation_file_path: path to the simulation file
    - dark_mode: True if dark mode is enabled
    """
    simulation_file_path_changed = pyqtSignal(str)
    simulation_file_status_changed = pyqtSignal(FileState)
    dark_mode_changed = pyqtSignal(bool)
    cursor_mode_changed = pyqtSignal(CursorMode)
    statusBar_message_changed = pyqtSignal(str)
    boundaries_loaded = pyqtSignal()
    origins_loaded = pyqtSignal()
    destinations_loaded = pyqtSignal()
    background_loaded = pyqtSignal(str)

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

    @property
    def cursor_mode(self):
        return self._cursor_mode
    
    @cursor_mode.setter
    def cursor_mode(self, value):
        self._cursor_mode = value
        self.cursor_mode_changed.emit(value)
        print('cursor_mode changed', value)

    @property
    def statusBar_message(self):
        return self._statusBar_message
    
    @statusBar_message.setter
    def statusBar_message(self, value):
        self._statusBar_message = value
        self.statusBar_message_changed.emit(value)

    @property
    def boundaries(self):
        return self._boundaries
    
    @boundaries.setter
    def boundaries(self, value):
        self._boundaries = value
        if value is not None:
            self.boundaries_loaded.emit()
            self._boundaries_table_model.updateData(value)

    def modify_boundaries(self, value):
        self._boundaries = value
        self._boundaries_table_model.updateData(value)


    @property
    def origins(self):
        return self._origins
    
    @origins.setter
    def origins(self, value):
        self._origins = value
        if value is not None:
            self.origins_loaded.emit()
            self._origins_table_model.updateData(value)

    @property
    def destinations(self):
        return self._destinations
    
    @destinations.setter
    def destinations(self, value):
        self._destinations = value
        if value is not None:
            self.destinations_loaded.emit()
            self._destinations_table_model.updateData(value)

    @property
    def boundaries_table_model(self):
        return self._boundaries_table_model

    @property
    def origins_table_model(self):
        return self._origins_table_model
    
    @property
    def destinations_table_model(self):
        return self._destinations_table_model

    @property
    def background(self):
        return self._background
    
    @background.setter
    def background(self, value):
        self._background = value
        self.background_loaded.emit(value)

    def __init__(self):
        super().__init__()
        self._geometry_file = None
        self._simulation_file_path = ''
        self._dark_mode = False
        self._simulation_file_status = FileState.UNCHANGED
        self._cursor_mode = CursorMode.POINTER
        self._statusBar_message = 'Ready'
        self._boundaries = None
        self._origins = None
        self._destinations = None
        self._boundaries_table_model = PolygonsTableModel(pd.DataFrame(columns=['id', 'points']))
        self._origins_table_model = PolygonsTableModel(pd.DataFrame(columns=['id', 'points']))
        self._destinations_table_model = PolygonsTableModel(pd.DataFrame(columns=['id', 'points']))
        self._background = None