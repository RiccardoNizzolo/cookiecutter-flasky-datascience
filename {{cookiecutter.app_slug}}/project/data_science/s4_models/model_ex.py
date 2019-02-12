from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from project.data_science.s4_models.abc_model import ABcModel
from sklearn.model_selection import train_test_split
import numpy as np
import lightgbm as lgbm

class LinearReg(ABcModel):


    def fit(self,x=None,y=None):
        self.train_error=np.inf
        for alpha in np.arange(0,1,0.1):
            #task_todo manage validation technique
            model=Ridge(alpha=alpha)
            model.fit(x,y)
            error=mean_squared_error(model.predict(x),y)
            if error<self.train_error:

                self.model=model
                self.best_alpha=alpha
                self.train_error=error


    def predict(self,x):
        return self.model.predict(x)

class lightGBMRegression(ABcModel):
    """
    example class of regression with lightgbm trained with early stopping on validation set
    """

    def fit(self,x=None,y=None):
        params = {
            'objective': 'regression',
            'learning_rate': 0.2,
            'num_leaves': 12,
            'feature_fraction': 1.00,
            'bagging_fraction': 0.8,
            'boosting_type': 'gbdt'
        }

        X_train, X_valid, Y_train, Y_valid = train_test_split(x, y,shuffle=False ,
                                                              test_size=0.33)

        # making lgbm datasets for train and valid
        d_train = lgbm.Dataset(X_train, Y_train)
        d_valid = lgbm.Dataset(X_valid, Y_valid)

        # training with early stop
        self.model = lgbm.train(params, d_train, 5000, valid_sets=[d_valid], verbose_eval=50, early_stopping_rounds=100)


    def predict(self, x):
        return self.model.predict(x)
