from dataAccess.dbConnection import DbConnection
from exceptions.businessException import BusinessException
from exceptions.responseCodes import ResponseCodes

class ItemsDA:
    @staticmethod
    def add(name, price, categoryId):
        fields_names = '(name, price, category_id)'
        values = '("' + name + '",' + str(price) + ',' + str(categoryId) + ')'
        query = 'INSERT INTO items ' + fields_names + ' VALUES ' + values
        db = DbConnection()
        cursor = db.connection.cursor()
        cursor.execute(query)
        last_index = cursor.lastrowid
        db.connection.commit()
        db.closeConnection() 
        return last_index

    @staticmethod
    def update(id, name, price, categoryId):
        query = 'UPDATE items SET name = "' + name +'", price = ' + str(price) + ', category_id = ' + str(categoryId) + ' WHERE id = ' + str(id)
        db = DbConnection()
        cursor = db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        db.closeConnection() 
        return

    @staticmethod
    def delete(id):
        query = 'DELETE FROM items WHERE id = ' + str(id)
        db = DbConnection()
        cursor = db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        db.closeConnection() 
        return

    @staticmethod
    def get(id, throwException = True):
        query = 'SELECT * FROM items WHERE id = ' + str(id)
        db = DbConnection()
        cursor = db.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        db.closeConnection()
        if data is None:
            if throwException : 
                raise BusinessException(ResponseCodes.itemNotFound)
            return None
        return data

    @staticmethod
    def getList(pageNumber, pageSize):
        query = 'SELECT * FROM items ORDER BY id LIMIT ' + str(pageSize) + ' OFFSET ' + str(pageSize * (pageNumber-1))
        db = DbConnection()
        cursor = db.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        db.closeConnection()
        return data
