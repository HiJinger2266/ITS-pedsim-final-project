import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QWidget
from PyQt5.QtCore import pyqtSlot
from views.agents_editor_ui import Ui_Dialog
from model.enums import FileState
from model.main_model import MainModel
from controllers.main_ctrl import MainController

class AgentsEditor(QDialog):
    def __init__(self, model: MainModel, main_controller: MainController):
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        