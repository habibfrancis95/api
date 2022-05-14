from models.resultObject import ResultObject
from exceptions.responseCodes import ResponseCodes
from exceptions.responseMessages import ResponseMessages


class GeneralWrapper:
    @staticmethod
    def successResult(data, language = None):
        return ResultObject(ResponseCodes.success, ResponseMessages.english[ResponseCodes.success], data)

    @staticmethod
    def errorResult(code, message):
        return ResultObject(code, message, {})
