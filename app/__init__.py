from flask import Flask

from app.misc.log import log


def register_extensions(flask_app: Flask):
    from app.extension import jwt, main_db

    jwt.init_app(flask_app)
    main_db.init_app(flask_app)


def register_views(flask_app: Flask):
    from app.views import route

    route(flask_app)


def register_hooks(flask_app: Flask):
    from app.hooks.request_context import after_request

    flask_app.after_request(after_request)


def create_app(*config_cls) -> Flask:
    log(message='Flask application intialized with {}'.format(', '.join([config.__name__ for config in config_cls])),
        keyword='INFO')

    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    register_extensions(flask_app)
    register_views(flask_app)
    register_hooks(flask_app)

    return flask_app
