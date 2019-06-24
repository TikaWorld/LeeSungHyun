from flask import Flask
from flask_restful import Api

from app.extension import Base, jwt
from app.views.adminAPI import AdminAPI
from app.views.projectAPI import ProjectAPI
from app.views.projectAPI import ProjectLIstAPI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/leepository?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = 'super-secret'
Base.init_app(app)
jwt.init_app(app)

api = Api(app)
api.add_resource(ProjectAPI, "/project/<string:project_name>")
api.add_resource(ProjectLIstAPI, "/projects")
api.add_resource(AdminAPI, "/login")


if __name__ == '__main__':
    app.run(debug=True)
