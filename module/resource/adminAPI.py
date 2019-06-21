from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource


class AdminAPI(Resource):

    @staticmethod
    def post():
        response = {}
        if not request.form:
            return {"msg": "Missing JSON in request"}, 400

        username = request.form['username']
        password = request.form['password']
        if not username:
            return {"msg": "Missing username parameter"}, 400
        if not password:
            return {"msg": "Missing password parameter"}, 400

        if username != 'test' or password != 'test':
            return {"msg": "Bad username or password"}, 401

        # Identity can be any data that is json serializable
        response["access_token"] = create_access_token(identity=username)

        return response, 200
