from flask_restful import Resource

from module.repository import project
from module.repository.projectRepository import ProjectRepository


class Project(Resource):
    def __init__(self):
        self.projectRepository = ProjectRepository()

    def get(self, project_name):
#        return self.projectRepository.getProject(project_name)
        return project.Project.query.filter_by(project_name="test").all()

#    def post(self):
#        return NotImplemented
