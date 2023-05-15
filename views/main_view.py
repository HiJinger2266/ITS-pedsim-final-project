from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow
import qdarkstyle

class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        # set stylesheet
        palette = qdarkstyle.Palette()
        palette.ID = "light"
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))

        # connect widgets to controller
        self._ui.actionToggle_Dark_Mode.triggered.connect(self._main_controller.toggle_dark_mode)

        # listen for model event signals
        self._model.simulation_file_changed.connect(self.on_simulation_file_changed)
        self._model.dark_mode_changed.connect(self.on_dark_mode_changed)

        self._ui.actionEdit_Signal.trggered.connect(self._edit_signal)

    @pyqtSlot(str)
    def on_simulation_file_changed(self, value):
        """
        This slot is called when the simulation_file property of the model changes.
        """
        self._ui.statusbar.showMessage(f'Simulation File Opened: {value}')

    @pyqtSlot()
    def on_actionOpen_Simulation_triggered(self):
        """
        This slot is called when the user clicks the Open Simulation menu item.
        """
        # open file dialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Simulation File', '', 'Simulation Files (*.sim);;All Files (*)')
        if file_name:
            self._main_controller.open_simulation_file(file_name)

    @pyqtSlot(bool)
    def on_dark_mode_changed(self, value):
        """
        This slot is called when the dark_mode property of the model changes.
        """
        if value:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        else:
            palette = qdarkstyle.Palette()
            palette.ID = "light"
            self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=palette))

    def _edit_signal(self):
        self._signal_editor = SignalEditor()
        self._signal_editor.show()