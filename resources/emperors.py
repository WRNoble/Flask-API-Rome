from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse

import models

class EmperorList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParse()
        self.reqparse.add_argument(
            "title",
            required=True,
            help="No emperor name provided",
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'url',
            require=True,
            help="No URL provided",
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        return jsonify({'emperors': [{'title': 'Augustus Caesar'}]})

class Emperor(Resource):
    def get(self, id):
        return jsonify({'title': 'Augustus Caesar'})

    def put(self, id):
        return jsonify({'title': 'Augustus Caesar'})

    def delete(self, id):
        return jsonify({'title': 'Augustus Caesar'})

emperors_api = Blueprint('resource.emperors', __name__)
api = Api(emperors_api)
api.add_resource(
    EmperorList,
    '/api/v1/emperors',
    endpoint='emperors'
)

api.add_resource(
    Emperor,
    '/api/v1/emperors/<int:id>',
    endpoint='emperor'
)