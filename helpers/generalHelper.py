from exceptions.businessException import BusinessException

class GeneralHelper:
    
    @staticmethod
    def checkId(id, errorCode):
        if id is None or type(id) != int or id <= 0:
            raise BusinessException(errorCode)
    
    @staticmethod
    def checkString(s, errorCode):
        if s is None or type(s) != str or len(s) <= 0:
            raise BusinessException(errorCode)
    
    @staticmethod
    def checkNumber(n, errorCode, allowSmallerThanZero = True):
        if n is None or (type(n) != int and type(n) != float):
            raise BusinessException(errorCode)
        if not (allowSmallerThanZero) and n < 0:
            raise BusinessException(errorCode)

    @staticmethod
    def getHttpStatusCode(code):
        if code == '200':
            return 200
        if code == '500':
            return 500
        if code >= '400-00' and code <= '400-99':
            return 400
        if code >= '401-00' and code <= '401-99':
            return 401
        if code >= '403-00' and code <= '403-99':
            return 403
        if code >= '404-00' and code <= '404-99':
            return 404
        return 200

