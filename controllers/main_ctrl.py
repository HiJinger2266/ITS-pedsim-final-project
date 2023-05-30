from PyQt5.QtCore import QObject, pyqtSlot, QSettings, QDateTime
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from model.enums import FileState
from model.main_model import MainModel
from model.sim_model import SimModel
from views.canvas_items import PolygonItem
import os
import json

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
        # load simulation file to new model
        with open(value, 'r') as f:
            data = json.load(f)
            self._model.boundaries = data['boundaries']
            self._model.origins = data['origins']
            self._model.destinations = data['destinations']
            # change background to absolute path
            if data['background'] != '':
                self._model.background = os.path.abspath(data['background'])
            else:
                self._model.background = ''

        # set simulation file path
        self._model.simulation_file_path = value
        # set simulation file status
        self._model.simulation_file_status = FileState.UNCHANGED
        # status bar message
        self._model.statusBar_message = f'Loaded simulation file: {value}'
        # emit file_loaded signal
        self._model.loaded = True
        
    @pyqtSlot(bool)
    def new_simulation_file(self):
        """
        connect with main_view action_new_triggered
        """
        # check current simulation file status
        if self._model.simulation_file_status == FileState.MODIFIED:
            # ask for save
            reply = QMessageBox.question(None, 'Save Simulation File', 'Do you want to save the current simulation file?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.save_simulation_file()
            elif reply == QMessageBox.Cancel:
                return
            elif reply == QMessageBox.No:
                pass
        self._model.simulation_file_path = ''
        # set simulation file status
        self._model.dark_mode = self._settings.value('dark_mode', False, type=bool)
        # status bar message
        self.set_boundaries([])
        self.set_origins([])
        self.set_destinations([])
        self.set_background('')
        self._model.simulation_file_status = FileState.NEW
        self._model.loaded = True
        self._model.statusBar_message = 'New simulation'

    @pyqtSlot(bool)
    def save_simulation_file(self):
        """
        connect with main_view action_save_triggered
        """
        if self._model.simulation_file_path == '':
            # ask for new file path
            file_path, _ = QFileDialog.getSaveFileName(None, 'Save Simulation File', '', 'Simulation Files (*.sim);;All Files (*)')
            # validate file path
            if file_path:
                self._model.simulation_file_path = file_path
            else:
                return
        elif self._model.simulation_file_status == FileState.UNCHANGED:
            return
        
        # change background to relative path
        if self._model.background != '':
            self._model.background = os.path.relpath(self._model.background, os.path.dirname(self._model.simulation_file_path))
        print(self._model.background)

        # save simulation file
        with open(self._model.simulation_file_path, 'w') as f:
            json.dump({
                'boundaries': self._model.boundaries,
                'origins': self._model.origins,
                'destinations': self._model.destinations,
                'background': self._model.background
            }, f)
        self._model.simulation_file_status = FileState.UNCHANGED
        # status bar message
        self._model.statusBar_message = f'File saved: {self._model.simulation_file_path}, {QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")}'

    @pyqtSlot(bool)
    def close_simulation_file(self):
        """
        connect with main_view action_close_triggered
        """
        if self._model.simulation_file_status == FileState.MODIFIED:
            # ask for save
            reply = QMessageBox.question(None, 'Save Simulation File', 'Do you want to save the current simulation file?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.save_simulation_file()
            elif reply == QMessageBox.Cancel:
                return
            elif reply == QMessageBox.No:
                pass
        self._model.simulation_file_path = ''
        # set simulation file status
        self._model.dark_mode = self._settings.value('dark_mode', False, type=bool)
        # status bar message
        self.set_boundaries([])
        self.set_origins([])
        self.set_destinations([])
        self.set_background('')
        self._model.statusBar_message = 'Ready'
        self._model.simulation_file_status = FileState.CLOSED
        self._model.loaded = True

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
        boundaries = []
        for v in value:
            if isinstance(v, PolygonItem):
                boundaries.append(v.to_dict())
            else:
                boundaries.append(v)
        self._model.boundaries = boundaries
        self._model.simulation_file_status = FileState.MODIFIED

    @pyqtSlot(bool)
    def set_origins(self, value):
        origins = []
        for v in value:
            if isinstance(v, PolygonItem):
                origins.append(v.to_dict())
            else:
                origins.append(v)
        self._model.origins = origins
        self._model.simulation_file_status = FileState.MODIFIED

    @pyqtSlot(bool)
    def set_destinations(self, value):
        destinations = []
        for v in value:
            if isinstance(v, PolygonItem):
                destinations.append(v.to_dict())
            else:
                destinations.append(v)
        self._model.destinations = destinations
        self._model.simulation_file_status = FileState.MODIFIED

    @pyqtSlot(bool)
    def set_background(self, value):
        self._model.background = value
        self._model.simulation_file_status = FileState.MODIFIED

    @pyqtSlot(bool)
    def start_simulation(self):
        # 
        pass