from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse, inputs, fields, marshal, marshal_with

import models

emperor_fields = {
    'id': fields.Integer,
    'title': fields.String,
}


class EmperorList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "title",           
            help="No emperor name provided",
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        emperors = [marshal(emperor, emperor_fields) for emperor in models.Emperor.select()]
        return {'emperors': emperors}

    def post(self):
        args = self.reqparse.parse_args()
        #models.Emperor.create(**args)
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