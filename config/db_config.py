import os

DB_NAME = 'leepository'


class LocalDBConfig:
    MAIN_DB_URL = 'mysql+pymysql://root:password123@localhost/{}?charset=utf8'.format(
        DB_NAME
    )


class RemoteDBConfig:
    MAIN_DB_URL = 'mysql+pymysql://{}:{}@{}:3306/{}?charset=utf8mb4'.format(
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_ENDPOINT'),
        DB_NAME
    )
