from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.models.project import Project


def list2str(list_data):
    result = ":".join(list_data)
    return result


class Projects(Resource):

    @staticmethod
    def get():
        response = {"list": [], "code": ""}
        result = Project.query.all()
        for project in result:
            response["list"].append(project.as_dict())
        response["code"] = "200"

        return response

    @staticmethod
    @jwt_required
    def post():
        response = {}
        project_name = request.form["project_name"]
        admission_grade = request.form["admission_grade"]
        developer_list = list2str(request.form.getlist("developer_list"))
        project_image = request.form["project_image"].encode()
        video_url = request.form["video_url"]
        content = request.form["content"]

        new_project = Project(project_name, admission_grade, developer_list, project_image, video_url, content)
        new_project.insert_or_update()
        response["code"] = "200"

        return response
