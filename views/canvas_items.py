import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyle

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

    @classmethod
    def from_dict(self, dict_):
        polygon = PolygonItem(color=dict_['color'])
        polygon.set_start_point(QtCore.QPointF(float(dict_['points'][0]['x']), float(dict_['points'][0]['y'])))
        for point in dict_['points'][1:-1]:
            polygon.add_point(QtCore.QPointF(float(point['x']), float(point['y'])))
        polygon.set_end_point(QtCore.QPointF(float(dict_['points'][-1]['x']), float(dict_['points'][-1]['y'])))
        polygon.id_ = dict_['id']

        return polygon
    
    def to_dict(self):
        dict_ = {}
        dict_['id'] = self.id_
        dict_['color'] = self.color
        dict_['points'] = []
        for point in self._points:
            dict_['points'].append({'x': str(point.x()), 'y': str(point.y())})
        return dict_

    def set_start_point(self, point):
        self.start_point = point
        self._points.append(point)

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

    def paint(self, painter, option, widget=None):
        """
        override the selected state to draw the item as selected
        """
        is_selected = option.state & QStyle.State_Selected
        option.state &= ~QStyle.State_Selected
        super().paint(painter, option, widget)
        
        if is_selected:
            # set brush to transparent
            painter.setBrush(QtGui.QBrush(QtCore.Qt.transparent))
            # set pen to yellow
            painter.setPen(QtGui.QPen(QtGui.QColor("yellow"), 2))
            # draw the rect bounding box of the polygon
            painter.drawRect(self.boundingRect())
            # show id on left top corner with black color
            painter.setPen(QtGui.QPen(QtGui.QColor("black"), 2))
            painter.setFont(QtGui.QFont('Arial', 12))
            text_pos = self.boundingRect().topLeft() + QtCore.QPointF(15, 25)
            painter.drawText(text_pos, f'id: {self.id_}')
            # restore the option state
            option.state |= QStyle.State_Selected

        
    
    @property
    def points(self):
        points_ = ''
        for point in self._points:
            points_ += f'(x:{point.x()}, y:{point.y()}), '
        return points_
    
    def hoverEnterEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor("yellow"), 2))
        #self.setCursor(QtCore.Qt.PointingHandCursor)
        super(PolygonItem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setPen(QtGui.QPen(QtGui.QColor(self.color), 2))
        #self.setCursor(QtCore.Qt.ArrowCursor)
        super(PolygonItem, self).hoverLeaveEvent(event)

    def random_point(self):
        """
        return a random point inside the polygon
        """
        x_min, x_max = self.boundingRect().left(), self.boundingRect().right()
        y_min, y_max = self.boundingRect().top(), self.boundingRect().bottom()
        while True:
            x = random.uniform(x_min, x_max)
            y = random.uniform(y_min, y_max)
            point = QtCore.QPointF(x, y)
            if self.contains(point):
                return point

    # def __getstate__(self):
    #     state = self.__dict__.copy()
    #     state_super = super(PolygonItem, self).__dict__.copy()
    #     state_all = {**state, **state_super}
    #     return state_all
    
    # def __setstate__(self, state):
        
    #     self.__dict__.update(state)
    #     super(PolygonItem, self).__init__(None)
    #     super(PolygonItem, self).__dict__.update(state)

class AgentItem(QtWidgets.QGraphicsEllipseItem):
    ID = 0
    def __init__(self, parent=None, color=None):
        super(AgentItem, self).__init__(parent)
        self.setZValue(20)
        if color is None:
            self.color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            self.color = QtGui.QColor(color)
        self.setPen(QtGui.QPen(QtGui.QColor(self.color), 2))
        self.setBrush(QtGui.QBrush(QtGui.QColor(self.color)))

        AgentItem.ID += 1
        self.id_ = AgentItem.ID
        self.radius = 5
        self.setRect(QtCore.QRectF(-self.radius, -self.radius, 2*self.radius, 2*self.radius))
