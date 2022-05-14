import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import os

class DbConnection:
    def __init__(self):
        self.connection = MySQLdb.connect(host = os.environ.get('DB_HOST'),
                                        user = os.environ.get('DB_USER'),
                                        password = os.environ.get('DB_PASSWORD'),
                                        db=os.environ.get('DB_NAME'))
    
    def closeConnection(self):
        self.connection.close()

