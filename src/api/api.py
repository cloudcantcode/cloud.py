"""
rest api with flask for get birb photos, i/o users stuff, and the souls of the lost childrens

"""
from flask import Flask
from flask_restful import Resource, Api
from imager import Imager  # IGNORE THIS BULLSHIT, JUST IGNORE PLEASE
import sys
sys.path.append("..")


app = Flask(__name__)
api = Api(app)
# test
img = Imager()
files = img.get_files()


class Bot(Resource):
    def get(self, id):
        return {'msg': f"I fucked your mom {id} times"}  # change this


api.add_resource(Bot, '/img/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
