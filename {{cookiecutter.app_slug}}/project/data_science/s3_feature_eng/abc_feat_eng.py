from abc import ABC, abstractmethod


class ABcFeatEng(ABC):
    """
    Abstract Base Class (ABC) for feature engineering
    """

    @abstractmethod
    def fit(self,data):
        pass

    @abstractmethod
    def transform(self,data):
        return data

    def fit_transform(self,data):
        self.fit(data)
        return self.transform(data)

