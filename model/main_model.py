from PyQt5.QtCore import QObject, pyqtSignal, QPointF
import pandas as pd
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
    file_loaded = pyqtSignal()
    boundaries_changed = pyqtSignal()
    origins_changed = pyqtSignal()
    destinations_changed = pyqtSignal()
    background_changed = pyqtSignal()
    mouse_coord_changed = pyqtSignal(QPointF)

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
            self.boundaries_changed.emit()
            self._boundaries_table_model.updateData(value)

    @property
    def origins(self):
        return self._origins
    
    @origins.setter
    def origins(self, value):
        self._origins = value
        if value is not None:
            self.origins_changed.emit()
            self._origins_table_model.updateData(value)

    @property
    def destinations(self):
        return self._destinations
    
    @destinations.setter
    def destinations(self, value):
        self._destinations = value
        if value is not None:
            self.destinations_changed.emit()
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
        self.background_changed.emit()

    @property
    def loaded(self):
        return self._loaded
    
    @loaded.setter
    def loaded(self, value):
        self._loaded = value
        self.file_loaded.emit()

    @property
    def mouse_coord_scene(self):    
        return self._mouse_coord_scene

    @mouse_coord_scene.setter
    def mouse_coord_scene(self, value):
        self._mouse_coord_scene = value
        self.mouse_coord_changed.emit(value)

    def __init__(self):
        super().__init__()
        self._simulation_file_path = ''
        self._dark_mode = False
        self._simulation_file_status = FileState.UNCHANGED
        self._cursor_mode = CursorMode.POINTER
        self._statusBar_message = 'Ready'
        self._loaded = False

        self._boundaries = {}
        self._origins = {}
        self._destinations = {}
        self._boundaries_table_model = PolygonsTableModel(pd.DataFrame(columns=['id', 'points']))
        self._origins_table_model = PolygonsTableModel(pd.DataFrame(columns=['id', 'points']))
        self._destinations_table_model = PolygonsTableModel(pd.DataFrame(columns=['id', 'points']))
        self._background = ''

        self.mouse_coord_scene = QPointF(0, 0)