from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

from module.resource.project import Project

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/leepository?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

db.create_all()

api = Api(app)
api.add_resource(Project, "/project/<string:project_name>")


if __name__ == '__main__':
    app.run(debug=True)
