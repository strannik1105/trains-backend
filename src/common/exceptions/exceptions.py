from common.exceptions.error_codes import ErrorCodes


class BackendException(Exception):
    def __init__(self, error: ErrorCodes):
        self.error_code = error.value[0]
        self.status_code = error.value[1]
        self.description = error.value[2]
