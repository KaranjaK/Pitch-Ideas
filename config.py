from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kk:Wemadeit@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options= {
    'development': DevConfig,
    'production': ProdConfig
}