import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    RESTX_MASK_SWAGGER = False


class ProdConfig(Config):
    DEBUG = True
    MONGODB_URI = 'mongodb://mongodb:27017/project_management'


class LocalConfig(Config):
    DEBUG = True
    MONGODB_URI = 'mongodb://localhost:27017/project_management'


config_by_name = dict(
    prod=ProdConfig,
    local=LocalConfig
)
