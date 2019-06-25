from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.extension import main_db
from app.models.profile import Profile


class ProfileAPI(Resource):

    def get(self, profile_name):
        err = "Nonexistent Profile"
        session = main_db.session
        response = Profile.get_first_or_abort_on_none(session, Profile.project_name == profile_name, message=err)
        response = response.as_dict()

        return response, 200


class ProfileListAPI(Resource):

    def get(self):
        session = main_db.session
        response = {"list": [], "code": ""}
        result = Profile.get_all(session, None)
        for project in result:
            response["list"].append(project.as_dict())

        return response, 200

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
