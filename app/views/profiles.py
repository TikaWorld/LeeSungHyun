from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.models.profile import Profile


class Profiles(Resource):

    @staticmethod
    def get():
        response = {"list": [], "code": ""}
        result = Profile.query.all()
        for project in result:
            response["list"].append(project.as_dict())
        response["code"] = "200"

        return response

    @staticmethod
    @jwt_required
    def post():
        response = {}
        project_name = request.form["profile_name"]
        admission_grade = request.form["admission_grade"]
        project_image = request.form["profile_image"].encode()
        content = request.form["content"]

        new_profile = Profile(project_name, admission_grade, project_image, content)
        new_profile.insert_or_update()
        response["code"] = "200"

        return response
