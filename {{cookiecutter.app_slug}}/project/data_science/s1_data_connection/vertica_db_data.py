import vertica_python
import pandas as pd

from project.data_science.s1_data_connection.abc_data_connection import ABcDataInterface
from project.data_science import ds_config


class VerticaDbData(ABcDataInterface):
    @staticmethod
    def get_training_data():
        cxn = {"user": ds_config['VERTICA_USER'],
               "password": ds_config['VERTICA_PASSWORD'],
               "host": ds_config['VERTICA_HOST'],
               "port": ds_config['VERTICA_PORT'],
               "database": ds_config['VERTICA_DB']}

        engine = vertica_python.connect(**cxn)

        df = pd.read_sql('select * from test.prime_numbers', con=engine)
        df.set_index('number',drop=False,inplace=True)
        return df

    @staticmethod
    def get_production_data():
        return pd.read_excel(ds_config['BASE_PATH']+'/data/data_sample_prod.xlsx')

    @staticmethod
    def transform_production_payload(payload):
        df=pd.DataFrame(payload)
        df.set_index('number', drop=False,inplace=True)
        return df
