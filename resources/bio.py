from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse

import models

class BioList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'emperor',
            required=True,
            help="No bio info provided",
            location=["form", "json"]
        )
        super().__init__()

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