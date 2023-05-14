class Agent(object):
    def __init__(self):
        self._show = False
        self._pos_x_meter = 0
        self._pos_y_meter = 0
        self._level = 0         # elevated == 1, ground == 0, underground == -1
        self._speed = 0
        self._direction_deg = 0
    def position(self):
        return [self._pos_x_meter, self._pos_y_meter]
    
if __name__ == "__main__":
    wow = Agent()
    what = wow.position()
    print(wow.position())
    
    
#Bike, Ped