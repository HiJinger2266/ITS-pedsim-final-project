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
    PAN = 1
    SELECT = 2
    POINTER = 3
    ADD = 4
    DELETE = 5
    EDIT = 6