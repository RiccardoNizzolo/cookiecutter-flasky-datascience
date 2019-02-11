# project/server/server_config.py

import os
from os.path import dirname
basedir = os.path.abspath(os.path.dirname(__file__))
import yaml
from logging.config import dictConfig



class BaseConfig(object):
    """Base configuration."""

    APP_NAME = os.getenv("APP_NAME", "data_science_ci")
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    BASE_PATH=dirname(dirname(basedir))
    MODELS_PERSISTENCE_PATH=BASE_PATH + '/data/persisted_orchestrator/'
    LOGGING_CONFIG=BASE_PATH+'/project/config/config_logger.yaml'
    ORCHESTRATORS_SEED_FILE=BASE_PATH+'/project/data_science/orchestrator_seed.yaml'


    def load_config(self):
        with open(self.LOGGING_CONFIG, 'r') as stream:
            try:
                dictConfig(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)




class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///{0}".format(os.path.join(basedir, "../project/server/../server/dev.db"))
    )


class TestingConfig(BaseConfig):
    """Testing configuration."""

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL", "sqlite:///")
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    WTF_CSRF_ENABLED = True

