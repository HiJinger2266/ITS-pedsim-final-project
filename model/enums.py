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