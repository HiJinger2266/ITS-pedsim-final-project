from PyQt5.QtCore import QObject, pyqtSignal
from model.enums import DistType

class SimModel(QObject):

    ped_dist_changed = pyqtSignal(DistType)
    ped_dist_params_changed = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self._boundaries = []
        self._origins = []
        self._destinations = []
        self._pedestrians = []
        self._ped_dist = DistType.POISSON
        self._ped_dist_params = [30]
        self._time_step = 1
        self._sim_time = 10
        self._current_time = 0

    @property
    def boundaries(self):
        return self._boundaries
    
    @boundaries.setter
    def boundaries(self, value):
        self._boundaries = value

    @property
    def origins(self):
        return self._origins

    @origins.setter
    def origins(self, value):
        self._origins = value

    @property
    def destinations(self):
        return self._destinations
    
    @destinations.setter
    def destinations(self, value):
        self._destinations = value

    @property
    def ped_dist(self):
        return self._ped_dist
    
    @ped_dist.setter
    def ped_dist(self, value):
        self._ped_dist = value
        self.ped_dist_changed.emit(value)

    @property
    def ped_dist_params(self):
        return self._ped_dist_params
    
    @ped_dist_params.setter
    def ped_dist_params(self, value):
        self._ped_dist_params = value
        self.ped_dist_params_changed.emit(value)

    @property
    def time_step(self):
        return self._time_step
    
    @time_step.setter
    def time_step(self, value):
        self._time_step = value

    @property
    def sim_time(self):
        return self._sim_time
    
    @sim_time.setter
    def sim_time(self, value):
        self._sim_time = value

    @property
    def current_time(self):
        return self._current_time
    
    @current_time.setter
    def current_time(self, value):
        self._current_time = value

    @property
    def pedestrians(self):
        return self._pedestrians
    
    @pedestrians.setter
    def pedestrians(self, value):
        self._pedestrians = value