from project.data_science.s3_feature_eng.abc_feat_eng import ABcFeatEng


class ScalingFeatEng(ABcFeatEng):
    """
    example class of a standard scaling feature eng
    """

    def fit(self, data):
        self.mean = data.mean()
        self.std = data.std()

    def transform(self, data):
        return (data - self.mean).multiply(1 / self.std)
