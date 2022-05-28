from app import app
from os import environ


if __name__ == '__main__':
    SERVER_HOST = environ.get('SERVER_HOST', '0.0.0.0')
    port = int(os.environ.get("PORT", 5000))
    app.run(host=SERVER_HOST,port=port, debug=True,threaded=True)
#(not environ.get('ENV') == 'PRODUCTION')