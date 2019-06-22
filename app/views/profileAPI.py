from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.models.profile import Profile


class ProfileAPI(Resource):

    def get(self, profile_name):
        response = Profile.query.filter_by(profile_name=profile_name).first()
        if response:
            response = response.as_dict()
            response["code"] = "200"
        else:
            response = Profile("", "", "").as_dict()
            response["code"] = "400"
        return response


class ProfileListAPI(Resource):

    def get(self):
        response = {"list": [], "code": ""}
        result = Profile.query.all()
        for project in result:
            response["list"].append(project.as_dict())
        response["code"] = "200"

        return response

    @jwt_required
    def post(self):
        response = {}
        project_name = request.form["profile_name"]
        admission_grade = request.form["admission_grade"]
        project_image = request.form["profile_image"].encode()
        content = request.form["content"]

        new_profile = Profile(project_name, admission_grade, project_image, content)
        new_profile.insert_or_update()
        response["code"] = "200"

        return response
