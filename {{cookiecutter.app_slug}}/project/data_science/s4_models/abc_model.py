from abc import ABC, abstractmethod


class ABcModel(ABC):
    """
    Abstract Base Class (ABC) for model
    """

    @abstractmethod
    def fit(self,data):
        pass

    @abstractmethod
    def predict(self,data):
        return data.sum(axis=1)*0


