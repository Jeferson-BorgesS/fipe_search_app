class FipeError(Exception):
    pass

class FipeConnectionError(FipeError):
    pass

class FipeDataError(FipeError):
    pass