from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


puppies = []


class PuppyNames(Resource):

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
