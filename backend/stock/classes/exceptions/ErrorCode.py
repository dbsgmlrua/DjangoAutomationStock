from enum import Enum, auto

class ErrorCode(enum):
    NO_ADMIN = auto()
    NOT_CONNECTED = auto()
    NOT_TRADE_INIT = auto()
    REQUEST_STATUS_OVER = auto()
    def __str__(self):
        return self.name