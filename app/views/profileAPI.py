from flask_restful import Resource

from app.models.profile import Profile


class ProfileAPI(Resource):

    @staticmethod
    def get(profile_name):
        response = Profile.query.filter_by(profile_name=profile_name).first()
        if response:
            response = response.as_dict()
            response["code"] = "200"
        else:
            response = Profile("", "", "").as_dict()
            response["code"] = "400"
        return response
