from app.db.DbHelper import DbHelper

class TasksDAO(object):
    __db = None;

    def __init__(self):
        self.__db = DbHelper()

    def getAll(self):
        return self.__db.query("SELECT * FROM tasks", None).fetchall();

    def create(self, params):
        self.__db.insert("INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)", (params.get('title'), params.get('description'), params.get('status')))

    def update(self, id, params):
        self.__db.insert("UPDATE tasks SET status = %s WHERE _id = %s", (params.get('status'), id))