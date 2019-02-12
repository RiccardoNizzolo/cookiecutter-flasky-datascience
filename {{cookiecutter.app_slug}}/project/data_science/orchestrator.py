import logging
from werkzeug.utils import import_string, ImportStringError
import pandas as pd

from decorators.decorators import  timer


log=logging.getLogger(__name__)





class Orchestrator():

    BASE_CLASSPATH='project.data_science.'

    def __init__(self, seed=None):
        self.meta=seed
        self.data_inteface=self.import_from_string(self.meta.get('data_inteface'))()
        self.target_generator=self.import_from_string(self.BASE_CLASSPATH + self.meta.get('target_generator'))()
        self.feat_eng=self.import_from_string(self.BASE_CLASSPATH + self.meta.get('feat_eng'))()
        self.model=self.import_from_string(self.BASE_CLASSPATH + self.meta.get('model'))()
        self.train_test_split = self.import_from_string(self.BASE_CLASSPATH + self.meta.get('train_test_split'))
        self.score_metric =  self.import_from_string(self.meta.get('score_metric'))
        return

    def import_from_string(self,str):

        try:
            return import_string(self.BASE_CLASSPATH+str)
        except ImportStringError:
            pass
        try:
            return  import_string(str)
        except ImportStringError:
            raise ImportStringError("The object doesn't have such attribute") from None

    @timer
    def build(self, data_limit=None):
        """
        Build the model
        :param data_limit:
        :return:
        """

        data=self.data_inteface.get_training_data()
        if data_limit is not None:
            data=data.head(data_limit)

        log.debug('loaded training data. shape: %s',data.shape)
        self.meta.update({'training_data_shape':str(data.shape)})

        online_data,y=self.target_generator.generate_target(data)
        self.data_interface = online_data.dtypes
        log.debug('generated production data like from training data. shape: %s', online_data.shape)

        train,test,y_train,y_test=self.train_test_split(online_data,y)
        log.debug('executed train test split. train shape: %s  test shape: %s', train.shape,test.shape)
        self.meta.update({'train set lines': str(y_train.shape)})
        self.meta.update({'test set lines': str(y_test.shape)})


        x_train= self.feat_eng.fit_transform(train)
        log.debug('generated engineered train data. shape: %s', x_train.shape)
        log.debug('engineered data types: \n%s', x_train.dtypes.value_counts())

        x_test= self.feat_eng.transform(test)

        log.debug('generated engineered train data. shape: %s', x_train.shape)

        self.model.fit(x=x_train,y=y_train)
        y_test_pred=self.model.predict(x=x_test)
        self.meta.update({'test_score':self.score_metric(y_test,y_test_pred)})
        log.info('score on test set %s', self.meta.get('test_performance'))

        return

    def predict(self,online_data):

        try:
            pd.testing.assert_series_equal(online_data.dtypes, self.data_interface)
        except:
            TypeError ('prediction data are not compatible with train data. check /<modelname>/data')
        log.debug('input production data shape: %s', online_data.shape)
        X = self.feat_eng.transform(online_data)
        log.debug('generated engineered train data. shape: %s',  X.shape)
        return self.model.predict(X)


    def payload_predict(self,payload):
        data=self.data_inteface.transform_production_payload(payload)
        data['prediction']=self.predict(data)
        return data['prediction'].to_dict()



