from flask_restful import Resource

from app.models.project import Project


class ProjectAPI(Resource):

    @staticmethod
    def get(project_name):
        response = Project.query.filter_by(project_name=project_name).first()
        if response:
            response = response.as_dict()
            response["code"] = "200"
        else:
            response = Project("", "", "").as_dict()
            response["code"] = "400"
        return response
