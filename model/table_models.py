import typing
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, QObject, QModelIndex, Qt

class DataFrameTableModel(QAbstractTableModel):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._data = pd.DataFrame()

    def data(self, index: QModelIndex, role: int):
        row_ = index.row()
        col_ = index.column()
        if role == Qt.DisplayRole:
            return str(self._data.iloc[row_, col_])
        
    def rowCount(self, parent: QModelIndex):
        return self._data.shape[0]
    
    def columnCount(self, parent: QModelIndex):
        return self._data.shape[1]
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]
            else:
                return section + 1
        return super().headerData(section, orientation, role)


class BoundariesTableModel(DataFrameTableModel):

    def __init__(self, data, parent=None) -> None:
        super().__init__(parent)
        self._data = data
    
    def updateData(self, boundaries):
        self.beginResetModel()
        df = pd.DataFrame(columns=['id', 'x1', 'y1', 'x2', 'y2'])
        for i, boundary in enumerate(boundaries):
            df.loc[i] = [boundary.id_, boundary.start_point.x(), boundary.start_point.y(), boundary.end_point.x(), boundary.end_point.y()]
        df['id'] = df['id'].astype(int)
        self._data = df
        # update the view
        self.endResetModel()    

class PolygonsTableModel(DataFrameTableModel):

    def __init__(self, data, parent=None) -> None:
        super().__init__(parent)
        self._data = data

    def updateData(self, polygon):
        self.beginResetModel()
        df = pd.DataFrame(columns=['id', 'points'])
        for i, o in enumerate(polygon):
            df.loc[i] = [o.id_, o.points]
        self._data = df
        # update the view
        self.endResetModel()