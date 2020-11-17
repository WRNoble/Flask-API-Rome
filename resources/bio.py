from flask import jsonify

from flask.ext.restful import Resource

import models

class BioList(Resource):
    def get(self):
        return jsonify({'bio': [{'life': 'The first emperor of Rome'}]})

class Bio(Resource):
    def get(self, id):
        return jsonify({'life': 'The first emperor of Rome'})

    def put(self, id):
        return jsonify({'life': 'The first emperor of Rome'})

    def delete(self, id):
        return jsonify({'life': 'The first emperor of Rome'})