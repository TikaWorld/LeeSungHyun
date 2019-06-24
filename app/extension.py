from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from app.models import MainDB

main_db = MainDB()
jwt = JWTManager()
