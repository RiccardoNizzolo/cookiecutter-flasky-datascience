import yaml
from project.config.server_config import BaseConfig
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
    DATA_FOLDER = os.environ.get("DATA_FOLDER",DsBaseConfig.BASE_PATH + '/data/')
    DATADB_USER=os.environ.get(
        "DATADB_USER", "dbadmin")
    DATADB_PASSWORD=os.environ.get(
        "DATADB_USER", "dbadmin")
    DATADB_HOST=os.environ.get(
        "DATADB_HOST", "localhost")
    DATADB_PORT=os.environ.get(
        "DATADB_PORT", 5433)
    DATADB_DB=os.environ.get(
        "DATADB_DB", 'docker')



class DsTestingConfig(DsBaseConfig):
    """Testing configuration."""
    STARTUP_RETRAIN = os.environ.get(
        "STARTUP_RETRAIN", False)
    DATA_FOLDER = os.environ.get("DATA_FOLDER", DsBaseConfig.BASE_PATH + '/data/')
    DATADB_USER = os.environ.get(
        "DATADB_USER", "dbadmin")
    DATADB_PASSWORD = os.environ.get(
        "DATADB_USER", "dbadmin")
    DATADB_HOST = os.environ.get(
        "DATADB_HOST", "localhost")
    DATADB_PORT = os.environ.get(
        "DATADB_PORT", 5433)
    DATADB_DB = os.environ.get(
        "DATADB_DB", 'docker')


class DsProductionConfig(DsBaseConfig):
    """Production configuration."""
    STARTUP_RETRAIN = os.environ.get(
        "STARTUP_RETRAIN", False)
    DATA_FOLDER = os.environ.get("DATA_FOLDER")
    DATADB_USER = os.environ.get(
        "DATADB_USER")
    DATADB_PASSWORD = os.environ.get(
        "DATADB_USER")
    DATADB_HOST = os.environ.get(
        "DATADB_HOST")
    DATADB_PORT = os.environ.get(
        "DATADB_PORT")
    DATADB_DB = os.environ.get(
        "DATADB_DB")

