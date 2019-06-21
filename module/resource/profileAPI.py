from flask_restful import Resource

from module.model.profile import Profile


class ProfileAPI(Resource):

    @staticmethod
    def get(project_name):
        response = Profile.query.filter_by(projectName=project_name).first()
        if response:
            response = response.as_dict()
            response["code"] = "200"
        else:
            response = Profile("", "", "").as_dict()
            response["code"] = "400"
        return response
