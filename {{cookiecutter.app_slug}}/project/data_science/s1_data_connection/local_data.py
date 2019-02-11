import pandas as pd

from project.data_science.s1_data_connection.abc_data_connection import ABcDataInterface
from project.data_science import ds_config

class LocalData(ABcDataInterface):
    @staticmethod
    def get_training_data():

        return pd.read_excel(ds_config['BASE_PATH']+'/data/data_sample.xlsx')

    @staticmethod
    def get_production_data():
        return pd.read_excel(ds_config['BASE_PATH']+'/data/data_sample_prod.xlsx')

    @staticmethod
    def transform_production_payload(payload):
        df = pd.DataFrame(payload)
        return df



if __name__=='__main__':

    print(LocalData().get_training_data())