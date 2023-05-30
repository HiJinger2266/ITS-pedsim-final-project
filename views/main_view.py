from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel
from PyQt5.QtCore import pyqtSlot, QSettings, Qt, QDateTime, QTimer
from PyQt5.QtGui import QKeySequence, QIcon
from views.main_view_ui import Ui_MainWindow
from views.signal_editor import SignalEditor
from views.agents_editor import AgentsEditor
from views.canvas import Canvas
from views.canvas_items import AgentItem, PolygonItem
from model.enums import FileState, CursorMode
from model.main_model import MainModel
from controllers.main_ctrl import MainController
import qdarkstyle
import tempfile
import os, sys


IMG_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'img')

class MainView(QMainWindow):
    def __init__(self, model: MainModel, main_controller: MainController):
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.simulation_time_label = QLabel()
        self._ui.statusbar.addPermanentWidget(self.simulation_time_label)
        self.mouse_coord_label = QLabel()
        self._ui.statusbar.addPermanentWidget(self.mouse_coord_label)
        self._ui.tableView.setModel(self._model.boundaries_table_model)
        # change canvas
        del self._ui.canvas
        self._ui.canvas = Canvas(self._ui.centralwidget, model=self._model, controller=self._main_controller)
        self._ui.canvas.setObjectName("canvas")
        self._ui.gridLayout.addWidget(self._ui.canvas, 0, 0, 1, 1)
        # load settings
        self._settings = QSettings('NTU', 'PedSim')
        # add toolbars
        self._ui.toolBar_file = self.addToolBar("File")
        self._ui.toolBar_edit = self.addToolBar("Edit")
        self._ui.toolBar_view = self.addToolBar("View")
        self._ui.toolBar_settings = self.addToolBar("Settings")
        self._ui.toolBar_run = self.addToolBar("Run")
        # add actions to toolbars
        self._ui.toolBar_file.addAction(self._ui.action_new)
        self._ui.toolBar_file.addAction(self._ui.action_open)
        self._ui.toolBar_file.addAction(self._ui.action_save)
        self._ui.toolBar_file.addAction(self._ui.action_close)
        self._ui.toolBar_file.addAction(self._ui.action_reload)
        
        self._ui.toolBar_edit.addAction(self._ui.action_edit_simulation)
        # self._ui.toolBar_edit.addAction(self._ui.action_edit_signal)
        # self._ui.toolBar_edit.addAction(self._ui.action_edit_agents)
        # self._ui.toolBar_edit.addAction(self._ui.action_edit_road)
        self._ui.toolBar_edit.addAction(self._ui.action_edit_bound)
        self._ui.toolBar_edit.addAction(self._ui.action_edit_origin)
        self._ui.toolBar_edit.addAction(self._ui.action_edit_destination)

        self._ui.toolBar_view.addAction(self._ui.action_pan)
        self._ui.toolBar_view.addAction(self._ui.action_pointer)
        self._ui.toolBar_view.addAction(self._ui.action_fit)

        self._ui.toolBar_settings.addAction(self._ui.action_toggle_dark_mode)

        self._ui.toolBar_run.addAction(self._ui.action_start)
        self._ui.toolBar_run.addAction(self._ui.action_pause)
        self._ui.toolBar_run.addAction(self._ui.action_stop)

        # toggle toolbars
        self._ui.action_toggle_toolbar_edit.triggered.connect(lambda: self._ui.toolBar_edit.setVisible(self._ui.action_toggle_toolbar_edit.isChecked()))
        self._ui.action_toggle_toolbar_view.triggered.connect(lambda: self._ui.toolBar_view.setVisible(self._ui.action_toggle_toolbar_view.isChecked()))
        self._ui.action_toggle_toolbar_settings.triggered.connect(lambda: self._ui.toolBar_settings.setVisible(self._ui.action_toggle_toolbar_settings.isChecked()))
        self._ui.action_toggle_toolbar_file.triggered.connect(lambda: self._ui.toolBar_file.setVisible(self._ui.action_toggle_toolbar_file.isChecked()))
        self._ui.action_toggle_toolbar_run.triggered.connect(lambda: self._ui.toolBar_run.setVisible(self._ui.action_toggle_toolbar_run.isChecked()))

        self._ui.comboBox.currentIndexChanged.connect(lambda x:self.change_table_view(x))
        self._signal_editor = SignalEditor(self._model, self._main_controller)
        self._agents_editor = AgentsEditor(self._model, self._main_controller)

        # set stylesheet
        palette = qdarkstyle.Palette()
        palette.ID = "light"
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))

        # connect widgets to controller
        self._ui.action_toggle_dark_mode.triggered.connect(self._main_controller.toggle_dark_mode)

        # listen for model event signals
        self._model.simulation_file_path_changed.connect(self.on_simulation_file_path_changed)
        self._model.simulation_file_status_changed.connect(self.on_simulation_file_status_changed)
        self._model.dark_mode_changed.connect(self.on_dark_mode_changed)
        self._model.cursor_mode_changed.connect(self.on_cursor_mode_changed)
        self._model.statusBar_message_changed.connect(lambda x: self.on_statusBar_message_changed(x))
        self._model.boundaries_changed.connect(self.on_boundaries_changed)
        self._model.origins_changed.connect(self.on_origins_changed)
        self._model.destinations_changed.connect(self.on_destinations_changed)
        self._model.mouse_coord_changed.connect(self.on_mouse_coord_changed)

        # connect menu items
        self._ui.action_edit_signal.triggered.connect(self._edit_signal)
        self._ui.action_edit_agents.triggered.connect(self._edit_agents)
        self._ui.action_start.triggered.connect(self._start)
        self._ui.action_pause.triggered.connect(self._pause)
        self._ui.action_stop.triggered.connect(self._stop)

        ## set initial state
        self._ui.action_close.setEnabled(False)
        self._ui.action_save.setEnabled(False)
        self._ui.action_edit_signal.setEnabled(False)
        self._ui.action_edit_agents.setEnabled(False)
        self._ui.action_edit_simulation.setEnabled(False)
        self._ui.action_edit_bound.setEnabled(False)
        self._ui.action_edit_origin.setEnabled(False)
        self._ui.action_edit_destination.setEnabled(False)
        self._ui.action_edit_road.setEnabled(False)
        self._ui.menuEdit_Geometry.setEnabled(False)
        self._ui.action_reload.setEnabled(False)
        self._ui.action_start.setEnabled(False)
        self._ui.action_pause.setEnabled(False)
        self._ui.action_stop.setEnabled(False)
        
        if self._settings.value('dark_mode', type=bool) is None:
            self._settings.setValue('dark_mode', False)
        # set dark mode
        if self._settings.value('dark_mode', type=bool):
            self._main_controller.toggle_dark_mode(True)

        # keyboard shortcuts
        self._ui.action_save.setShortcut(QKeySequence('Ctrl+S'))


    @pyqtSlot(str)
    def on_simulation_file_path_changed(self, value):
        """
        This slot is called when the simulation_file_path property of the model changes.
        """
        self._main_controller.set_statusBar_message('Simulation file changed: {}'.format(value))

    @pyqtSlot(FileState)
    def on_simulation_file_status_changed(self, value):
        """
        This slot is called when the simulation_file_status property of the model changes.
        """
        if value == FileState.UNCHANGED:
            # make actions available
            self._ui.action_close.setEnabled(True)
            self._ui.action_save.setEnabled(True)
            self._ui.action_edit_signal.setEnabled(True)
            self._ui.action_edit_agents.setEnabled(True)
            self._ui.action_edit_simulation.setEnabled(True)
            self._ui.menuEdit_Geometry.setEnabled(True)
            self._ui.action_reload.setEnabled(True)
            self._ui.action_edit_road.setEnabled(True)
            self._ui.action_edit_bound.setEnabled(True)
            self._ui.action_edit_origin.setEnabled(True)
            self._ui.action_edit_destination.setEnabled(True)
            self._ui.action_start.setEnabled(True)
            self._ui.action_pause.setEnabled(False)
            self._ui.action_stop.setEnabled(False)
            # set title
            self.setWindowTitle(f'PedSim - {self._model.simulation_file_path}')
            # self._ui.statusbar.showMessage(f'{self._model.simulation_file_path}, last saved {QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")}')
            self._main_controller.set_statusBar_message(f'{self._model.simulation_file_path}, last saved {QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")}')
        elif value == FileState.MODIFIED:
            # make actions available
            self._ui.action_close.setEnabled(True)
            self._ui.action_save.setEnabled(True)
            self._ui.action_edit_signal.setEnabled(True)
            self._ui.action_edit_agents.setEnabled(True)
            self._ui.action_edit_simulation.setEnabled(True)
            self._ui.menuEdit_Geometry.setEnabled(True)
            self._ui.action_reload.setEnabled(True)
            self._ui.action_edit_road.setEnabled(True)
            self._ui.action_edit_bound.setEnabled(True)
            self._ui.action_edit_origin.setEnabled(True)
            self._ui.action_edit_destination.setEnabled(True)
            self._ui.action_start.setEnabled(True)
            self._ui.action_pause.setEnabled(False)
            self._ui.action_stop.setEnabled(False)
            # set title
            self.setWindowTitle(f'PedSim - {self._model.simulation_file_path} *')

        elif value == FileState.NEW:
            # make actions available
            self._ui.action_close.setEnabled(True)
            self._ui.action_save.setEnabled(True)
            self._ui.action_edit_signal.setEnabled(True)
            self._ui.action_edit_agents.setEnabled(True)
            self._ui.action_edit_simulation.setEnabled(True)
            self._ui.menuEdit_Geometry.setEnabled(True)
            self._ui.action_reload.setEnabled(True)
            self._ui.action_edit_road.setEnabled(True)
            self._ui.action_edit_bound.setEnabled(True)
            self._ui.action_edit_origin.setEnabled(True)
            self._ui.action_edit_destination.setEnabled(True)
            self._ui.action_start.setEnabled(True)
            self._ui.action_pause.setEnabled(False)
            self._ui.action_stop.setEnabled(False)
            # set title
            self.setWindowTitle(f'PedSim - {self._model.simulation_file_path} *')

        elif value == FileState.CLOSED:
            # make actions unavailable
            self._ui.action_close.setEnabled(False)
            self._ui.action_save.setEnabled(False)
            self._ui.action_edit_signal.setEnabled(False)
            self._ui.action_edit_agents.setEnabled(False)
            self._ui.action_edit_simulation.setEnabled(False)
            self._ui.menuEdit_Geometry.setEnabled(False)
            self._ui.action_reload.setEnabled(False)
            self._ui.action_edit_road.setEnabled(False)
            self._ui.action_edit_bound.setEnabled(False)
            self._ui.action_edit_origin.setEnabled(False)
            self._ui.action_edit_destination.setEnabled(False)
            self._ui.action_start.setEnabled(False)
            self._ui.action_pause.setEnabled(False)
            self._ui.action_stop.setEnabled(False)
            # set title
            self.setWindowTitle(f'PedSim')
            print('File closed')

    @pyqtSlot()
    def on_action_open_triggered(self):
        """
        This slot is called when the user clicks the Open Simulation menu item.
        """
        # open file dialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Simulation File', '', 'Simulation Files (*.sim);;All Files (*)')
        if file_name:
            self._main_controller.open_simulation_file(file_name)

    @pyqtSlot()
    def on_action_new_triggered(self):
        """
        This slot is called when the user clicks the New Simulation menu item.
        """
        self._main_controller.new_simulation_file()
        

    @pyqtSlot(bool)
    def on_dark_mode_changed(self, value):
        """
        This slot is called when the dark_mode property of the model changes.
        """
        if value:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self._ui.dockWidgetContents.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            # self._ui.action_toggle_dark_mode.setText('Light Mode')
            # self._ui.action_toggle_dark_mode.setIcon(QIcon(os.path.join(IMG_FOLDER, 'dark_mode_alt.svg')))
            # if windows:
            if sys.platform == 'win32':
                from ctypes import windll, byref, sizeof, c_int
                # set window title bar color
                HWND = self.winId().__int__()
                DWMWA_ATTRIBUTE = 35
                COLOR = 0x002d2319
                windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
    
        else:
            palette = qdarkstyle.Palette()
            palette.ID = "light"
            self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))
            self._ui.dockWidgetContents.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))
            # self._ui.action_toggle_dark_mode.setText('Dark Mode')
            # self._ui.action_toggle_dark_mode.setIcon(QIcon(os.path.join(IMG_FOLDER, 'dark_mode.svg')))
            if sys.platform == 'win32':
                from ctypes import windll, byref, sizeof, c_int
                # set window title bar color
                HWND = self.winId().__int__()
                DWMWA_ATTRIBUTE = 35
                COLOR = 0x00ffffff
                windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
            
            QIcon.setThemeSearchPaths([os.path.join(IMG_FOLDER)])


    def _edit_signal(self):
        self._signal_editor.show()

    def _edit_agents(self):
        self._agents_editor.show()

    @pyqtSlot()
    def on_action_pan_triggered(self):
        """
        This slot is called when the user clicks the Pan menu item.
        """
        self._main_controller.set_cursor_mode(CursorMode.PAN)

    @pyqtSlot()
    def on_action_pointer_triggered(self):
        """
        This slot is called when the user clicks the Pointer menu item.
        """
        self._main_controller.set_cursor_mode(CursorMode.POINTER)

    @pyqtSlot()
    def on_action_edit_bound_triggered(self):
        """
        This slot is called when the user clicks the Edit Bound menu item.
        """
        self._main_controller.set_cursor_mode(CursorMode.ADD_BOUNDARY)
        self._main_controller.set_statusBar_message('Click to add a bound line, press ESC to cancel.')

    @pyqtSlot()
    def on_action_save_triggered(self):
        """
        This slot is called when the user clicks the Save menu item.
        """
        self._main_controller.save_simulation_file()  

    @pyqtSlot()
    def on_action_close_triggered(self):
        """
        This slot is called when the user clicks the Close menu item.
        """
        self._main_controller.close_simulation_file()

    @pyqtSlot()
    def on_action_edit_origin_triggered(self):
        self._main_controller.set_cursor_mode(CursorMode.ADD_ORIGIN)  

    @pyqtSlot()
    def on_action_edit_destination_triggered(self):
        self._main_controller.set_cursor_mode(CursorMode.ADD_DESTINATION)

    @pyqtSlot()
    def on_action_background_triggered(self):
        """
        This slot is called when the user clicks the Background menu item.
        """
        # open file dialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Background Image', '', 'Image Files (*.png *.jpg *.bmp);;All Files (*)')
        if file_name:
            self._main_controller.set_background(file_name)
        self._ui.canvas.scene().set_background(file_name)
    
    @pyqtSlot(CursorMode)
    def on_cursor_mode_changed(self, value):
        """
        This slot is called when the cursor_mode property of the model changes.
        """
        if value == CursorMode.DELETE_LINE or value == CursorMode.DELETE_POLYGON:
            self._ui.canvas.setCursor(Qt.CursorShape.ForbiddenCursor)
        elif value == CursorMode.POINTER:
            self._ui.canvas.setCursor(Qt.CursorShape.ArrowCursor)
        elif value == CursorMode.ADD_BOUNDARY or value == CursorMode.ADD_ORIGIN or value == CursorMode.ADD_DESTINATION:
            self._ui.canvas.setCursor(Qt.CursorShape.CrossCursor)

    @pyqtSlot()
    def on_statusBar_message_changed(self, value):
        """
        This slot is called when the message property of the statusBar changes.
        """
        self.statusBar().showMessage(value)

    @pyqtSlot()
    def on_boundaries_changed(self):
        """
        This slot is called when the boundaries property of the model changes.
        """
        self._main_controller.set_statusBar_message('Boundaries changed.')
        self._ui.tableView.resizeColumnsToContents()

    @pyqtSlot()
    def on_origins_changed(self):
        """
        This slot is called when the origins property of the model changes.
        """
        self._main_controller.set_statusBar_message('Origins changed.')
        self._ui.tableView.resizeColumnsToContents()

    @pyqtSlot()
    def on_destinations_changed(self):
        """
        This slot is called when the destinations property of the model changes.
        """
        self._main_controller.set_statusBar_message('Destinations changed.')
        self._ui.tableView.resizeColumnsToContents()

    @pyqtSlot()
    def on_action_fit_triggered(self):
        """
        This slot is called when the user clicks the Fit menu item.
        """
        self._ui.canvas.fitInView(self._ui.canvas.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        
    def change_table_view(self, index):
        if index == 0:
            self._ui.tableView.setModel(self._model.boundaries_table_model)

        elif index == 1:
            self._ui.tableView.setModel(self._model.origins_table_model)
        
        elif index == 2:
            self._ui.tableView.setModel(self._model.destinations_table_model)
        self._ui.tableView.resizeColumnsToContents()

    def on_mouse_coord_changed(self, point):
        self.mouse_coord_label.setText(f'x: {int(point.x())}, y: {int(point.y())}')

    def _start(self):
        # self._main_controller.start_simulation()
        # test
        if len(self._model.origins) == 0:
            self._main_controller.set_statusBar_message('No origin defined.')
            return
        if hasattr(self,'isPaused'):
            if self.isPaused:
                self.isPaused = False
                self._ui.action_pause.setEnabled(True)
                self.timer.start(int(self.time_step*1000))
                return

        self.time_step = 0.1
        self.current_step = 0
        self.num_steps = 100
        self.simulation_time_label.setText(f'Simulation time: {self.current_step}')
        self.agents = []
        for i in range(20):
            agent = AgentItem()
            origin = PolygonItem.from_dict(self._model.origins[0])
            # random point inside origin
            point = origin.random_point()
            agent.setPos(point)
            self._ui.canvas.scene().addItem(agent)
            self.agents.append(agent)

        self._ui.action_pause.setEnabled(True)
        self._ui.action_start.setEnabled(False)
        self._ui.action_stop.setEnabled(True)
        # update every 0.1 second    
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(int(self.time_step * 1000))
        self._main_controller.set_statusBar_message('Simulation started.')

    def update_simulation(self):
        for agent in self.agents:
            # agent.setPos(agent.pos() + QPointF(1, 0))
            agent.move_to_destination(self._model.destinations[0])
        self.simulation_time_label.setText(f'Simulation time: {self.current_step * self.time_step:.2f}')
        self.current_step += 1
        if self.current_step > self.num_steps:
            self._stop()
            self._main_controller.set_statusBar_message('Simulation finished.')

    def _pause(self):
        self.timer.stop()
        self._ui.action_pause.setEnabled(False)
        self._ui.action_start.setEnabled(True)
        self._ui.action_stop.setEnabled(True)
        self._main_controller.set_statusBar_message('Simulation paused.')
        self.isPaused = True

    def _stop(self):
        self.timer.stop()
        self._ui.action_pause.setEnabled(False)
        self._ui.action_start.setEnabled(True)
        self._ui.action_stop.setEnabled(False)
        self._main_controller.set_statusBar_message('Simulation stopped.')
        for agent in self.agents:
            self._ui.canvas.scene().removeItem(agent)
        if hasattr(self, 'isPaused'):
            del self.isPaused