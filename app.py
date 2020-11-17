from flask import Flask

import models
from resources.emperors import emperors_api
from resources.bio import bio_api

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(emperors_api)
app.register_blueprint(bio_api, url_prefix='/api/v1')

@app.route('/')
def hello_world():
    return 'Hello'

if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)