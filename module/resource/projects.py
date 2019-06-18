from flask import request
from flask_restful import Resource

from module.model.project import Project


class Projects(Resource):

    def post(self):
        response = {}

        project_name = request.form["projectName"]
        admission_grade = request.form["admissionGrade"]
        developer_list = self.list2str(request.form["developerList"])
        project_image = request.form["projectImage"].encode()
        video_url = request.form["videoUrl"]
        content = request.form["content"]
        print(project_name, admission_grade, developer_list, project_image, video_url, content)

        new_project = Project(project_name, admission_grade, developer_list, project_image, video_url, content)
        print(new_project)
        new_project.add()
        response["result"] = "200"

        return response

    def list2str(self, list_data):
        result = ""
        for data in list_data:
            result = result + ":" + data
        return result
