from enum import Enum, auto
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

class ErrorCode(Enum):
    NO_ADMIN = auto()
    NOT_CONNECTED = auto()
    NOT_TRADE_INIT = auto()
    TOO_MANY_REQUEST = auto()
    REQUEST_ERROR = auto()
    INTERNAL_SERVER_ERROR = auto()
    def __str__(self):
        return self.name
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['message'] = response.data['detail']
        del response.data['detail']
    return response

#tooo long
def raise_exception_by_errorcode(errorcode):
    detail = None
    status_code = None
    print(ErrorCode.__members__)
    print(errorcode.name)
    # if errorcode == ErrorCode.NO_ADMIN:
    #     status_code = 500
    #     detail = errorcode.name
    # elif errorcode == ErrorCode.NOT_CONNECTED:
    #     status_code = 500
    #     detail = errorcode.name
    # elif errorcode == ErrorCode.NOT_TRADE_INIT:
    #     status_code = 500
    #     detail = errorcode.name
    # elif errorcode == ErrorCode.TOO_MANY_REQUEST:
    #     status_code = 500
    #     detail = errorcode.name
    # elif errorcode == ErrorCode.REQUEST_ERROR:
    #     status_code = 500
    #     detail = errorcode.name
    # elif errorcode == ErrorCode.INTERNAL_SERVER_ERROR:
    #     status_code = 500
    #     detail = errorcode.name
    # else :
    #     status_code = 500
    #     detail = "INTERNAL_SERVER_ERROR"

    

    if errorcode.name in ErrorCode.__members__:
        status_code = 500
        detail = errorcode.name
    else :
        status_code = 500
        detail = ErrorCode.INTERNAL_SERVER_ERROR.name

    raise CustomApiException(status_code, detail)


class CustomApiException(APIException):
    #public fields
    detail = None
    status_code = None

    # create constructor
    def __init__(self, status_code, message):
        #override public fields
        CustomApiException.status_code = status_code
        CustomApiException.detail = message