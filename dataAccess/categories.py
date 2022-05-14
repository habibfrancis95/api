from dataAccess.dbConnection import DbConnection
from exceptions.businessException import BusinessException
from exceptions.responseCodes import ResponseCodes

class CategoriesDA:
    @staticmethod
    def get(id, throwException = True):
        query = 'SELECT * FROM categories WHERE id = ' + str(id)
        db = DbConnection()
        cursor = db.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        db.closeConnection()
        if data is None:
            if throwException : 
                raise BusinessException(ResponseCodes.categoryNotFound)
            return None
        return data