class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MYSQL_HOST = "localhost"
    # MYSQL_PORT = "3306"
    # MYSQL_USERNAME = "username"
    # MYSQL_PASSWORD = "password"
    # MYSQL_DATABASE = "database-name"
    #
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST,
    #                                                                   MYSQL_PORT, MYSQL_DATABASE)
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     'pool_size': 300,
    #     'pool_pre_ping': True,
    #     'pool_recycle': 3600
    #
    # }