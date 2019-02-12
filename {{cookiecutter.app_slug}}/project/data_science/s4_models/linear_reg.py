from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from project.data_science.s4_models.abc_model import ABcModel
import numpy as np

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