from flask_restful import Resource


class MainAPI(Resource):
    def get(self):
        return "Welcome LeeSunghyun project which Introduce DSM Project!", 200
