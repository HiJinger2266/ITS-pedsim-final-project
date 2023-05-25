from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, pyqtSignal
from PyQt5.QtWidgets import QGraphicsSceneWheelEvent
from model.enums import CursorMode
from model.main_model import MainModel
from controllers.main_ctrl import MainController
from views.canvas_items import PolygonItem

class Canvas(QtWidgets.QGraphicsView):

    factor = 1.25

    def __init__(self, parent=None, model=None, controller=None):
        super(Canvas, self).__init__(parent)
        self.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        self.setMouseTracking(True)
        QtWidgets.QShortcut(QtGui.QKeySequence.ZoomIn, self, activated=self.zoom_in)
        QtWidgets.QShortcut(QtGui.QKeySequence.ZoomOut, self, activated=self.zoom_out)
        self.setScene(CanvasScene(self, model, controller))
        self.model = model
        self.controller = controller

        self.model.cursor_mode_changed.connect(self.set_cursor_mode)

    def zoom_in(self):
        self.zoom(Canvas.factor)

    def zoom_out(self):
        self.zoom(1 / Canvas.factor)
    
    def zoom(self, f):
        self.scale(f, f)

    def wheelEvent(self, event: QGraphicsSceneWheelEvent):
        if event.angleDelta().y() > 0:
            self.zoom(Canvas.factor)
        else:
            self.zoom(1 / Canvas.factor)

        super(Canvas, self).wheelEvent(event)

    def set_cursor_mode(self, mode):
        if mode == CursorMode.PAN:
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        else:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)

class CanvasScene(QtWidgets.QGraphicsScene):

    def __init__(self, parent=None, model: MainModel=None, controller: MainController=None):
        super(CanvasScene, self).__init__(parent)
        self.image_item = QtWidgets.QGraphicsPixmapItem()
        self.image_item.setZValue(-1)
        ## for debugging
        self.image_item.setPixmap(QtGui.QPixmap())
        self.addItem(self.image_item)
        self.model = model
        self.controller = controller
        self.boundary = None
        self.origin = None
        self.destination = None
        self.boundaries = []
        self.origins = []
        self.destinations = []
        self.set_current_mode(self.model.cursor_mode)
        
        self.model.cursor_mode_changed.connect(self.set_current_mode)
        self.model.file_loaded.connect(self.load_file)
        

    def load_file(self):
        self.image_item.setPixmap(QtGui.QPixmap(self.model.background))
        self.setSceneRect(self.image_item.boundingRect())
        for boundary in self.boundaries:
            self.removeItem(boundary)
        for origin in self.origins:
            self.removeItem(origin)
        for destination in self.destinations:
            self.removeItem(destination)
        self.boundaries = []
        self.origins = []
        self.destinations = []
        for boundary in self.model.boundaries:
            boundary_ = PolygonItem.from_dict(boundary)
            self.addItem(boundary_)
            self.boundaries.append(boundary_)
        for origin in self.model.origins:
            origin_ = PolygonItem.from_dict(origin)
            self.addItem(origin_)
            self.origins.append(origin_)
        for destination in self.model.destinations:
            destination_ = PolygonItem.from_dict(destination)
            self.addItem(destination_)
            self.destinations.append(destination_)

        self.set_current_mode(self.model.cursor_mode)

    def set_current_mode(self, mode):
        self.current_mode = mode
        if mode == CursorMode.ADD_BOUNDARY:
            if self.boundary is not None:
                self.removeItem(self.boundary)
                self.boundary = None
            self._change_selectable(False)
        if mode == CursorMode.POINTER:
            self._change_selectable(True)
        if mode == CursorMode.ADD_ORIGIN:
            if self.origin is not None:
                self.removeItem(self.origin)
                self.origin = None
            self._change_selectable(False)
        if mode == CursorMode.ADD_DESTINATION:
            if self.destination is not None:
                self.removeItem(self.destination)
                self.destination = None
            self._change_selectable(False)
        if mode == CursorMode.PAN:
            self._change_selectable(False)

    def _change_selectable(self, selectable: bool):
        for boundary in self.boundaries:
            boundary.setAcceptHoverEvents(selectable)
            boundary.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, selectable)
            # boundary.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, selectable)
            boundary.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, selectable)
        for origin in self.origins:
            origin.setAcceptHoverEvents(selectable)
            origin.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, selectable)
            # origin.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, selectable)
            origin.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, selectable)
        for destination in self.destinations:
            destination.setAcceptHoverEvents(selectable)
            destination.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, selectable)
            # destination.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, selectable)
            destination.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, selectable)

    def set_background(self, image_path):
        self.image_item.setPixmap(QtGui.QPixmap(image_path))
        # self.addItem(self.image_item)
        self.setSceneRect(self.image_item.boundingRect())

    def mousePressEvent(self, event):
        if self.current_mode == CursorMode.ADD_BOUNDARY:
            if self.boundary is None:
                self.boundary = PolygonItem(color='blue')
                self.addItem(self.boundary)
                self.boundary.set_start_point(event.scenePos())
            else:
                # if right click, finish drawing
                if event.button() == QtCore.Qt.RightButton:
                    self.boundary.set_end_point(event.scenePos())
                    self.boundaries.append(self.boundary)
                    self.controller.set_boundaries(self.boundaries)
                    self.boundary = None
                else:
                    self.boundary.add_point(event.scenePos())
                    self.controller.set_boundaries(self.boundaries)

        elif self.current_mode == CursorMode.ADD_ORIGIN:
            if self.origin is None:
                self.origin = PolygonItem()
                self.addItem(self.origin)
                self.origin.set_start_point(event.scenePos())
            else:
                # if right click, finish drawing
                if event.button() == QtCore.Qt.RightButton:
                    self.origin.set_end_point(event.scenePos())
                    self.origins.append(self.origin)
                    self.controller.set_origins(self.origins)
                    self.origin = None
                else:
                    self.origin.add_point(event.scenePos())

        elif self.current_mode == CursorMode.ADD_DESTINATION:
            if self.destination is None:
                self.destination = PolygonItem(color='orange')
                self.addItem(self.destination)
                self.destination.set_start_point(event.scenePos())
            else:
                # if right click, finish drawing
                if event.button() == QtCore.Qt.RightButton:
                    self.destination.set_end_point(event.scenePos())
                    self.destinations.append(self.destination)
                    self.controller.set_destinations(self.destinations)
                    self.destination = None
                else:
                    self.destination.add_point(event.scenePos())

        return super(CanvasScene, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        self.model.mouse_coord_scene = event.scenePos()
        if self.current_mode == CursorMode.ADD_BOUNDARY:
            if self.boundary is not None:
                self.boundary.set_end_point(event.scenePos(), temp=True)
        elif self.current_mode == CursorMode.ADD_ORIGIN:
            if self.origin is not None:
                self.origin.set_end_point(event.scenePos(), temp=True)
        elif self.current_mode == CursorMode.ADD_DESTINATION:
            if self.destination is not None:
                self.destination.set_end_point(event.scenePos(), temp=True)
            
        super(CanvasScene, self).mouseMoveEvent(event)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            if self.boundary is not None:
                self.removeItem(self.boundary)
                self.boundary = None
            if self.origin is not None:
                self.removeItem(self.origin)
                self.origin = None
            if self.destination is not None:
                self.removeItem(self.destination)
                self.destination = None
        if event.key() == QtCore.Qt.Key_Delete:
            if self.selectedItems():
                for item in self.selectedItems():
                    if isinstance(item, PolygonItem):
                        if item in self.boundaries:
                            self.boundaries.remove(item)
                            self.controller.set_boundaries(self.boundaries)
                        if item in self.origins:
                            self.origins.remove(item)
                            self.controller.set_origins(self.origins)
                        elif item in self.destinations:
                            self.destinations.remove(item)
                            self.controller.set_destinations(self.destinations)
                    self.removeItem(item)
        
        return super(CanvasScene, self).keyPressEvent(event)