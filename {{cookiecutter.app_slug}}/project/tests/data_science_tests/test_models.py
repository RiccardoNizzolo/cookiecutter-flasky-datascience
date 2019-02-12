from project.data_science.orchestrator import Orchestrator
from project.config.data_science_config import DataScienceOrcherstratorConfig
import pandas as pd
from unittest import TestCase
import numpy as np

class  TestOrchestrators(TestCase):


    def test_fast_training_should_works(self):
        for model_name, orchestrator in self.get_untrained_models().items():
            orchestrator.build(data_limit=1000)


    def test_predict_is_idempotent(self):
        for model_name, orchestrator in self.get_untrained_models().items():
            orchestrator.build(data_limit=1000)
            data = orchestrator.data_inteface.get_training_data().tail(1000)
            online_data, _ = orchestrator.target_generator.generate_target(data)

            incremental_load=[]
            num_chuncks=10
            chunk_list= [online_data[i:i+num_chuncks] for i in range(0,online_data.shape[0],num_chuncks)]
            for chunk in chunk_list:
                incremental_load=np.concatenate([incremental_load,orchestrator.predict(chunk)])

            full_load = orchestrator.predict(online_data)

            np.testing.assert_almost_equal(full_load,incremental_load,decimal=12,err_msg='Model '+model_name+ 'failed idempotence test')



    def get_untrained_models(self):

        orchestrators={}
        for model_name, seed in DataScienceOrcherstratorConfig().get_dict().items():
            orc = Orchestrator(seed)
            orc.build()
            orchestrators.update({model_name : orc})

        return orchestrators

    def dataframe_upsert(self,original_df,new_data_df):
        return pd.concat([original_df[~original_df.index.isin(new_data_df.index)], new_data_df])


