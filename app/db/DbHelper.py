import pymysql.cursors
import pymysql

class DbHelper:

    __connection = None;
    __cursor = None;

    def __init__(self):
        __db_config = "mysql";
        self.__connection = pymysql.connect(host="162.241.2.230",
                                            user = "hestco05_george",
                                            password = "!Q2w3e4r5t",
                                            db = "hestco05_george",
                                            charset = 'utf8mb4',
                                            cursorclass = pymysql.cursors.DictCursor);
        self.__cursor = self.__connection.cursor();

    def query(self, query, params):
       self.__cursor.execute(query, params)
       return self.__cursor;

    def insert(self, query, params):
        self.__cursor.execute(query, params)
        self.__connection.commit()

    def close(self):
        self.__connection.close();