import json

from flask import Flask
from flask_cors import CORS

from config import BaseConfig
from rest import initialize_api

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
CORS(app)

initialize_api(app)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)