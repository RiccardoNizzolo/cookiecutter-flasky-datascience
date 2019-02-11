from flask.config import Config
import os

ds_settings = os.getenv(
    "DS_SETTINGS", "project.config.data_science_config.DsDevelopmentConfig"
)

ds_config=Config(None)
ds_config.from_object(ds_settings)