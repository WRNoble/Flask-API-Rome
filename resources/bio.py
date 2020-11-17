from flask import jsonify, Blueprint

from flask_restful import Resource, Api

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


bio_api = Blueprint('resources.bio', __name__)
api = Api(bio_api)
api.add_resource(
    BioList,
    '/bios',
    endpoint='bios'
)

api.add_resource(
    Bio,
    '/bios/<int:id>',
    endpoint="bio"
)