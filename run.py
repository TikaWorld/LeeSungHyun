from app import create_app
from config.db_config import LocalDBConfig
from constants.local_run import RUN_SETTING

app = create_app(LocalDBConfig)

if __name__ == '__main__':
    app.run(**RUN_SETTING)
