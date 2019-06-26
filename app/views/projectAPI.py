from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.extension import main_db
from app.models.project import Project


class ProjectAPI(Resource):

    def get(self, project_name):
        err = "Nonexistent Project"
        session = main_db.session
        response = Project.get_first_or_abort_on_none(session, Project.project_name == project_name, message=err)
        response = response.as_dict()

        return response, 200


def list2str(list_data):
    result = ":".join(list_data)
    return result


class ProjectLIstAPI(Resource):
    def get(self):
        session = main_db.session
        response = {"list": [], "code": ""}
        result = Project.get_all(session, None)
        for project in result:
            response["list"].append(project.as_dict())

        return response, 200

    @jwt_required
    def post(self):
        response = {}
        session = main_db.session
        project_name = request.form["project_name"]
        admission_grade = request.form["admission_grade"]
        developer_list = list2str(request.form.getlist("developer_list"))
        project_image = request.form["project_image"].encode()
        video_url = request.form["video_url"]
        content = request.form["content"]

        new_project = Project(project_name, admission_grade, developer_list, project_image, video_url, content)
        session.add(new_project)
        session.commit()
        session.refresh(new_project)
        response["msg"] = "Success"

        return response, 200
