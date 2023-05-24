from PyQt5 import QtCore, QtGui, QtWidgets

class LineItem(QtWidgets.QGraphicsLineItem):

    ID = 0

    def __init__(self, parent=None, type_=''):
        super(LineItem, self).__init__(parent)
        self.setZValue(10)
        self.setPen(QtGui.QPen(QtGui.QColor("red"), 2))
        self.setAcceptHoverEvents(False)

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, False)
        LineItem.ID += 1
        self.id_ = LineItem.ID
        if type_ != '':
            self.type_ = type_
        else:
            self.type_ = 'line'

    def set_start_point(self, point):
        self.start_point = point
    
    def set_end_point(self, point, temp=False):
        self.end_point = point
        if temp:
            self.setPen(QtGui.QPen(QtGui.QColor("red"), 2, QtCore.Qt.DashLine))
            self.setLine(QtCore.QLineF(self.start_point, self.end_point))
        else:
            self.setPen(QtGui.QPen(QtGui.QColor("red"), 2))
            self.setLine(QtCore.QLineF(self.start_point, self.end_point))

    def hoverEnterEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor("yellow"), 2))
        self.setCursor(QtCore.Qt.PointingHandCursor)
        super(LineItem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor("red"), 2))
        #self.setCursor(QtCore.Qt.ArrowCursor)
        super(LineItem, self).hoverLeaveEvent(event)     

class RectItem(QtWidgets.QGraphicsRectItem):
    def __init__(self, parent=None):
        super(LineItem, self).__init__(parent)
        self.setZValue(10)
        self.setPen(QtGui.QPen(QtGui.QColor("blue"), 2))
        self.setAcceptHoverEvents(False)

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, False)

    def set_start_point(self, point):
        self.start_point = point

    def set_end_point(self, point, temp=False):
        self.end_point = point
        if temp:
            self.setPen(QtGui.QPen(QtGui.QColor("blue"), 2, QtCore.Qt.DashLine))
            self.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
            self.setRect(QtCore.QRectF(self.start_point, self.end_point))
        else:
            self.setPen(QtGui.QPen(QtGui.QColor("blue"), 2))
            self.setBrush(QtGui.QBrush(QtGui.QColor("blue")))
            self.setRect(QtCore.QRectF(self.start_point, self.end_point))

    def hoverEnterEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor("yellow"), 2))
        self.setCursor(QtCore.Qt.PointingHandCursor)
        super(LineItem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor("blue"), 2))
        self.setCursor(QtCore.Qt.ArrowCursor)
        super(LineItem, self).hoverLeaveEvent(event)

class PolygonItem(QtWidgets.QGraphicsPolygonItem):
    ID = 0
    def __init__(self, parent=None, color='green'):
        super(PolygonItem, self).__init__(parent)
        self.setZValue(10)
        self.color = color
        self.setPen(QtGui.QPen(QtGui.QColor(self.color), 2))
        self.setAcceptHoverEvents(False)

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, False)

        self._points = []
        PolygonItem.ID += 1
        self.id_ = PolygonItem.ID

    def set_start_point(self, point):
        self.start_point = point

    def add_point(self, point):
        self._points.append(point)
    
    def set_end_point(self, point, temp=False):
        self.end_point = point
        if temp:
            self.setPen(QtGui.QPen(QtGui.QColor(self.color), 2, QtCore.Qt.DashLine))
            self.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
            self.setPolygon(QtGui.QPolygonF(self._points + [self.end_point]))

        else:
            self.setPen(QtGui.QPen(QtGui.QColor(self.color), 2))
            self.setBrush(QtGui.QBrush(QtGui.QColor(self.color)))
            self._points.append(point)
            self.setPolygon(QtGui.QPolygonF(self._points))
    
    @property
    def points(self):
        points_ = ''
        for point in self._points:
            points_ += f'(x:{point.x()}, y:{point.y()}), '
        return points_
    
    def hoverEnterEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor("yellow"), 2))
        self.setCursor(QtCore.Qt.PointingHandCursor)
        super(PolygonItem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor(self.color), 2))
        self.setCursor(QtCore.Qt.ArrowCursor)
        super(PolygonItem, self).hoverLeaveEvent(event)
