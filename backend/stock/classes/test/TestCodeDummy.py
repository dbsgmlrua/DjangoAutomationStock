from stock.classes.exceptions.StockExceptionHandler import raise_exception_by_errorcode, ErrorCode

def ExceptionTestChecker(code):
    if True:
        return raise_exception_by_errorcode(ErrorCode.NOT_CONNECTED)
    else:
        return None