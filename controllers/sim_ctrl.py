from PyQt5.QtCore import QObject, pyqtSlot
from model.sim_model import SimModel

class SimController(QObject):
    def __init__(self, model: SimModel):
        super().__init__()

        self._model = model
        
    def new_sim(self):
        pass