"""
implementation examples of step 1 : data connection
"""
import pandas as pd
import vertica_python


from project.data_science.s1_data_connection.abc_data_connection import ABcDataInterface
from project.data_science import ds_config

class LocalData(ABcDataInterface):
    """
    Example class for loading data from file.

    """

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



class VerticaDbData(ABcDataInterface):
    """
    Example class for loading data from a database (vertica).

    """

    KEY= ['col1','col2']

    def get_connection(self):
        cnx_dict = {'user': ds_config['DATADB_USER'],
               "password": ds_config['DATADB_PASSWORD'],
               "host": ds_config['DATADB_HOST'],
               "port": ds_config['DATADB_PORT'],
               "database": ds_config['DATADB_DB'],
               }

        conn = vertica_python.connect(**cnx_dict)
        return conn

    @classmethod
    def get_training_data(cls):

        df =pd.read_sql('select * from test.prime_numbers', con=cls.get_connection())
        df.set_index(cls.KEY, drop=False)
        return df

    @classmethod
    def get_production_data(cls):
        df = pd.read_sql('select * from prod.prime_numbers', con=cls.get_connection())
        df.set_index(cls.KEY, drop=False)
        return df

    @classmethod
    def transform_production_payload(cls,payload):
        df = pd.DataFrame(payload)
        df.set_index(cls.KEY, drop=False)
        return df

