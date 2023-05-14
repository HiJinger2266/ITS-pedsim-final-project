from PyQt5.QtCore import QObject, pyqtSignal

class Agent(QObject):
    show_changed = pyqtSignal(bool)
    pos_x_meter_changed = pyqtSignal(float)
    pos_y_meter_changed = pyqtSignal(float)
    level_changed = pyqtSignal(int)
    speed_changed = pyqtSignal(float)
    direction_deg_changed = pyqtSignal(float)

    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, value):
        self._show = value
        self.show_changed.emit(value)

    @property
    def pos_x_meter(self):
        return self._pos_x_meter

    @pos_x_meter.setter
    def pos_x_meter(self, value):
        self._pos_x_meter = value
        self.pos_x_meter_changed.emit(value)

    @property
    def pos_y_meter(self):
        return self._pos_y_meter

    @pos_y_meter.setter
    def pos_y_meter(self, value):
        self._pos_y_meter = value
        self.pos_y_meter_changed.emit(value)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        self.level_changed.emit(value)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
        self.speed_changed.emit(value)

    @property
    def direction_deg(self):
        return self._direction_deg

    @direction_deg.setter
    def direction_deg(self, value):
        self._direction_deg = value
        self.direction_deg_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._show = False
        self._pos_x_meter = 0
        self._pos_y_meter = 0
        self._level = 0         # elevated == 1, ground == 0, underground == -1
        self._speed = 0
        self._direction_deg = 0

if __name__ == "__main__":
    # unit test
    agent = Agent()
    agent.show_changed.connect(lambda value: print("show changed: {}".format(value)))
    agent.pos_x_meter_changed.connect(lambda value: print("pos_x_meter changed: {}".format(value)))
    agent.pos_y_meter_changed.connect(lambda value: print("pos_y_meter changed: {}".format(value)))
    agent.level_changed.connect(lambda value: print("level changed: {}".format(value)))
    agent.speed_changed.connect(lambda value: print("speed changed: {}".format(value)))
    agent.direction_deg_changed.connect(lambda value: print("direction_deg changed: {}".format(value)))

    agent.show = True
    agent.pos_x_meter += 1
    agent.pos_y_meter += 1
    agent.level += 1
    agent.speed += 1
    agent.direction_deg += 1

    print(f"agent.show: {agent.show}")
    print(f"agent.pos_x_meter: {agent.pos_x_meter}")
    print(f"agent.pos_y_meter: {agent.pos_y_meter}")
    print(f"agent.level: {agent.level}")
    print(f"agent.speed: {agent.speed}")
    print(f"agent.direction_deg: {agent.direction_deg}")