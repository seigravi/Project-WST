from flask import Flask, request
from flask_restful import Resource, Api
import indicoio

app = Flask(__name__)
api = Api(app)
indicoio.config.api_key = "23a60181adf45bc35de426b6cb99ae73"

class Analyze(Resource):
    def get(self):
        batch = indicoio.sentiment(["I love writing code!", "I hate this project."])
        return batch

api.add_resource(Analyze, '/analyze')

if __name__ == '__main__':
     app.run(port='5002')