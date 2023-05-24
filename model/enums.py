from enum import Enum

class FileState(Enum):
    """
    FileState Enum
    """
    NEW = 1
    MODIFIED = 2
    DELETED = 3
    UNCHANGED = 4
    CLOSED = 5

class SignalState(Enum):
    """
    SignalState Enum
    """
    RED = 1
    YELLOW = 2
    GREEN = 3

class CursorMode(Enum):
    """
    CursorMode Enum
    """
    ADD_BOUNDARY = 1
    ADD_ORIGIN = 2
    DELETE_LINE = 3
    DELETE_POLYGON = 4
    MOVE_LINE = 5
    MOVE_POLYGON = 6
    POINTER = 7
    PAN = 8
    ADD_DESTINATION = 9