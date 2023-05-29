class Zone:
    def 
    (x1, y1)
    pass

class PedCrossing(Zone):    # 行人穿越線
    pass

class BikeCrossing(Zone):   # 自行車穿越線
    pass

class Sidewalk(Zone):       # 人行道，人車共道
    def __init__(self):
        pass
    
    def accommodate(self, agent):
        zone

class RoadLane(Zone):       # 車道
    pass

class Edge(Zone):
    pass

class SoftEdge(Edge):       # 彈性邊界，例如標線
    pass

class HardEdge(Edge):       # 硬性邊界，例如分隔島
    pass