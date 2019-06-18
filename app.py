from flask import Flask
from flask_restful import Api

from database import db
from module.resource.projectResource import ProjectResource
from module.resource.projects import Projects

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/leepository?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

api = Api(app)
api.add_resource(ProjectResource, "/project/<string:project_name>")
api.add_resource(Projects, "/projects")


if __name__ == '__main__':
    app.run(debug=True)
