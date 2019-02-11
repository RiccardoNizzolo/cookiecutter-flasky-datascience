import yaml
from config.server_config import BaseConfig
import os




class DataScienceOrcherstratorConfig():

    def __init__(self):

        file =BaseConfig().ORCHESTRATORS_SEED_FILE
        self.cfg = self.load_config(file)

    APP_NAME = os.getenv("APP_NAME", "data_science_ci")


    @staticmethod
    def load_config(config_file):
        with open(config_file, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_dict(self):
        return self.cfg

class DsBaseConfig(object):
    """Base configuration."""

    BASE_PATH=BaseConfig.BASE_PATH
    MODELS_PERSISTENCE_PATH=BASE_PATH + '/data/persisted_orchestrator/'
    LOGGING_CONFIG=BASE_PATH+'/project/config/config_logger.yaml'
    ORCHESTRATORS_SEED_FILE=BASE_PATH+'/project/data_science/orchestrator_seed.yaml'



class DsDevelopmentConfig(DsBaseConfig):
    """Development configuration."""
    STARTUP_RETRAIN=os.environ.get(
        "STARTUP_RETRAIN", True)
    VERTICA_USER=os.environ.get(
        "VERTICA_USER", "dbadmin")
    VERTICA_PASSWORD=os.environ.get(
        "VERTICA_USER", "dbadmin")
    VERTICA_HOST=os.environ.get(
        "VERTICA_HOST", "localhost")
    VERTICA_PORT=os.environ.get(
        "VERTICA_PORT", 5433)
    VERTICA_DB=os.environ.get(
        "VERTICA_DB", 'docker')



class DsTestingConfig(DsBaseConfig):
    """Testing configuration."""
    STARTUP_RETRAIN = os.environ.get(
        "STARTUP_RETRAIN", False)
    VERTICA_USER = os.environ.get(
        "VERTICA_USER", "dbadmin")
    VERTICA_PASSWORD = os.environ.get(
        "VERTICA_USER", "dbadmin")
    VERTICA_HOST = os.environ.get(
        "VERTICA_HOST", "localhost")
    VERTICA_PORT = os.environ.get(
        "VERTICA_PORT", 5433)
    VERTICA_DB = os.environ.get(
        "VERTICA_DB", 'docker')


class DsProductionConfig(DsBaseConfig):
    """Production configuration."""
    STARTUP_RETRAIN = os.environ.get(
        "STARTUP_RETRAIN", False)
    VERTICA_USER = os.environ.get(
        "VERTICA_USER")
    VERTICA_PASSWORD = os.environ.get(
        "VERTICA_USER")
    VERTICA_HOST = os.environ.get(
        "VERTICA_HOST")
    VERTICA_PORT = os.environ.get(
        "VERTICA_PORT")
    VERTICA_DB = os.environ.get(
        "VERTICA_DB")

