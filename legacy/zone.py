class Zone: (x1, y1)
    pass

class PedCrossing(Zone):    # 行人穿越線
    pass

class BikeCrossing(Zone):   # 自行車穿越線
    pass

class Sidewalk(Zone):       # 人行道，人車共道
    pass

class RoadLane(Zone):       # 車道
    pass

class Edge(Zone):
    pass

class SoftEdge(Edge):       # 彈性邊界，例如標線
    pass

class HardEdge(Edge):       # 硬性邊界，例如分隔島
    pass