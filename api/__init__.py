from flask import Flask

api = Flask(__name__)

if __name__ == '__main__':
    api.run(debug=True)

from api import routes