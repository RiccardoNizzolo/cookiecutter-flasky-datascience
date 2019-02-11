import pickle
from project.data_science.orchestrator import Orchestrator
from project.config.data_science_config import DataScienceOrcherstratorConfig
import os
from project.decorators.singleton import Singleton
from project.data_science import ds_config
from git.repo import Repo
import datetime





class DataScienceModelsPersistor(metaclass=Singleton):

    def __init__(self):

            self.folder=ds_config['MODELS_PERSISTENCE_PATH']

            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
            self.creation_date=datetime.datetime.now().isoformat()
            self.commit= self._check_repo_and_getcommit()
            self.filename=self.folder+self.commit+'_dsmodels.pkl'
            self._build_or_load()

    def _build_or_load(self):
        """
        at server startup choose between retraining or fast loading
        :return:
        """
        if (os.path.isfile(self.filename)) and not ds_config['STARTUP_RETRAIN']:
            self._load_models()
        else:
            self.build_models()

    def build_models(self):

        models={}
        for model_name, seed in DataScienceOrcherstratorConfig().get_dict().items():
            orc = Orchestrator(seed)
            orc.build()
            models.update({model_name : orc})

        self.models=models

        with open(self.filename, 'wb') as output:
            pickle.dump(models, output)

        return models



    def _load_models(self):

        with open(self.filename, 'rb') as output:
            models=pickle.load(output)
            self.models=models


    def _check_repo_and_getcommit(self):
        #TODO improve this logic. I would like to retrain not only for new commits but also fo new data.
        # Also add tests
        repo = Repo(search_parent_directories=True)
        if not repo.is_dirty() or True:
            return repo.head.object.hexsha
        else:
            raise ValueError('working directory is not clean! please commit before running the server')
