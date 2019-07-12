from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.extension import main_db
from app.models.student import Student


class StudentAPI(Resource):

    def get(self, student_name):
        err = "Nonexistent Profile"
        session = main_db.session
        response = Student.get_first_or_abort_on_none(session, Student.student_name == student_name, message=err)
        response = response.as_dict()

        return response, 200


class StudentListAPI(Resource):

    def get(self):
        session = main_db.session
        response = {"list": [], "code": ""}
        result = Student.get_all(session, None)
        for project in result:
            response["list"].append(project.as_dict())

        return response, 200

    @jwt_required
    def post(self):
        response = {}
        session = main_db.session
        student_name = request.form["student_name"]
        admission_grade = request.form["student_grade"]
        project_name = request.form["student_name"]
        project_image = request.form["student_image"].encode()
        content = request.form["content"]

        new_student = Student(student_name, admission_grade, project_name, project_image, content)
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        response["msg"] = "Success"

        return response, 200
