from PyQt5.QtCore import QObject, pyqtSlot

class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @pyqtSlot(bool)
    def open_simulation_file(self, value):
        print(value)
        self._model.simulation_file = value

    @pyqtSlot(bool)
    def toggle_dark_mode(self, value):
        self._model.dark_mode = not self._model.dark_mode