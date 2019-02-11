from project.data_science.orchestrator import Orchestrator
from project.config.data_science_config import DataScienceOrcherstratorConfig
import pandas as pd
from unittest import TestCase

class  TestOrchestrators(TestCase):

    def setUp(self):

        self.orchestrators =self._build_models()

    def test_online_data_interface_is_consistent(self):

        for model_name,model in self.orchestrators.items():
            data = model.data_inteface.get_training_data()
            train_data, y = model.target_generator.generate_target(data)

            online_data=model.data_inteface.get_production_data()

            pd.testing.assert_series_equal(train_data.dtypes,online_data.dtypes)

    def test_model_train_return_none(self):
        # task_todo
        pass

    def test_no_train_lines_in_test(self):
        # task_todo
        pass

    def test_predict_is_idempotent(self):
        # task_todo
        pass

    def test_predict_should_be_nan_resistent(self):
        # task_todo
        pass


    def _build_models(self):

        orchestrators={}
        for model_name, seed in DataScienceOrcherstratorConfig().get_dict().items():
            orc = Orchestrator(seed)
            orc.build()
            orchestrators.update({model_name : orc})

        self.orchestrators=orchestrators

        return orchestrators





