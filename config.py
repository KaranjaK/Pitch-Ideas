from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kk:Wemadeit@localhost/watchlist'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options= {
    'development': DevConfig,
    'production': ProdConfig
}