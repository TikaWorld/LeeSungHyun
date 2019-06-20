import json

from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource


class AdminAPI(Resource):

    def post(self):
        respones = {}
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
        respones["access_token"] = create_access_token(identity=username)

        return respones, 200
