from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)
# / users
users_path = './data/users.csv'


# / locations

class User(Resource):
    def get(self):
        data = pd.read_csv(users_path, on_bad_lines='skip')
        data = data.to_dict()
        return {'data': data}, 200

    def post(self):
        # initialize the parser
        parser = reqparse.RequestParser()
        # when we add the arguments into the request this is going to read them
        parser.add_argument('locationId', required=True, type=int)
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('city', required=True, type=str)
        # we have 3 arguments which user can post on API
        # now we extract what user sent
        args = parser.parse_args()
        # return{
        #     'loc': args['locationId'],
        #     'name': args['name'],
        #     'city': args['city']
        # }, 200

        data = pd.read_csv(users_path)

        if args['userId'] in data['userId']:
            return {
                'message': f"{args['userId']} already exists"
            }, 409
        else:
            data = data.append({
                'userId': args['userId'],
                'city': args['userId'],
                'name': args['userId'],
                'locations': []
            }, ignore_index=True)
            data.to_csv(users_path, index=False)
            return {'data': data.to_dict()}, 200


class Locations(Resource):
    pass


#  map class User to the /users place in the Api
# api.com/users
api.add_resource(User, '/users')
api.add_resource(Locations, '/locations')

if __name__ == "__main__":
    app.run(debug=True)
