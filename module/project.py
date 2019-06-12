from flask_restful import Resource
from module.projectRepository import ProjectRepository


class Project(Resource):
    def __init__(self):
        self.projectRepository = ProjectRepository()

    def get(self, name):
        return self.projectRepository.getProject(name)

    def post(self):
        return NotImplemented
