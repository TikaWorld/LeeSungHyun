import json

from flask_restful import Resource

from module.repository.project import Project
from module.repository.projectRepository import ProjectRepository


class ProjectResource(Resource):
    def __init__(self):
        self.projectRepository = ProjectRepository()

    def get(self, project_name):
#        return self.projectRepository.getProject(project_name)
        result = Project.query.all()
        print(result)
        return result

#    def post(self):
#        return NotImplemented
