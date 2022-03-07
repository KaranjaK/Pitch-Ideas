from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:

    pass

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options= {
    'development': DevConfig,
    'production': ProdConfig
}