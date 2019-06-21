from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

main_db = SQLAlchemy()
jwt = JWTManager()
