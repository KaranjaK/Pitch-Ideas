from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kk:Wemadeit@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options= {
    'development': DevConfig,
    'production': ProdConfig
}