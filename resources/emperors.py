from flask import jsonify

from flask.ext.restful import Resource

import models

class EmperorList(Resource):
    def get(self):
        return jsonify({'emperors': [{'title': 'Augustus Caesar'}]})

class Emperor(Resource):
    def get(self, id):
        return jsonify({'title': Augustus Caesar})

    def put(self, id):
        return jsonify({'title': Augustus Caesar})

    def delete(self, id):
        return jsonify({'title': Augustus Caesar})