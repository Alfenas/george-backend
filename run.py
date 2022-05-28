from app import app
from os import environ


if __name__ == '__main__':
    SERVER_HOST = environ.get('SERVER_HOST', 'app-george.herokuapp.com')
    app.run(host=SERVER_HOST, debug=(not environ.get('ENV') == 'PRODUCTION'),threaded=True)
