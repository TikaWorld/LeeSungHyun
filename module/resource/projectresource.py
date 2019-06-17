from flask_restful import Resource

from module.model.project import Project


class ProjectResource(Resource):

    def get(self, project_name):
        result = Project.query.filter_by(projectName=project_name).first()
        if result:
            result = result.as_dict()
            result["result"] = "200"
            return result
        else:
            return {"projectName": "", "admissionGrade": "", "projectImage": "", "": "", "content": "", "result": "400"}

    def post(self):
        return NotImplemented
