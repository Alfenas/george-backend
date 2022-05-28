from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS

from app.dao.tasksDAO import TasksDAO

app = Flask(__name__)
CORS(app)
api = Api(app, 
    version='1.0', 
    title='API George',
    description='API responsavel por tratamento de dados para o sistema *George*. Desenvolvimento: <a target="_blank" href="https://hest.com.br">hest tech</a>.',
)

ns = api.namespace('task', description='tasks operations')

todo = api.model('Task', {
    '_id': fields.Integer(readonly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='The task title'),
    'description': fields.String(required=True, description='The task description'),
    'status': fields.String(required=True, description='Status of task'),
})

tasksDAO = TasksDAO()

@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return tasksDAO.getAll()

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return tasksDAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return tasksDAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)