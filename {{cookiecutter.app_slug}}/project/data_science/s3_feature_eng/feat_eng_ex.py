from project.data_science.s3_feature_eng.abc_feat_eng import ABcFeatEng



class FeatEngIdentity(ABcFeatEng):
    """
    example class of a feature engineering that does nothing
    """

    def fit(self, data):
        pass

    def transform(self, data):
        return data



class FeatEngScaling(ABcFeatEng):
    """
    example class of a standard scaling feature eng
    """

    def fit(self, data):
        self.mean = data.mean()
        self.std = data.std()

    def transform(self, data):
        data = data.copy()
        return (data - self.mean).multiply(1 / self.std)


class FeatEngAddColumns(ABcFeatEng):
    """
    example class of a standard scaling feature eng
    """

    def fit(self, data):
            pass

    def transform(self, data):
        data=data.copy()
        data['x^2']=data['x1']*data['x1']
        return data

