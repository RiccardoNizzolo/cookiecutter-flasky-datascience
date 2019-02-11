from abc import ABC, abstractmethod, abstractproperty


class ABcDataInterface(ABC):
    """
    Abstract Base Class (ABC) for reading and loading data
    """


    @abstractmethod
    def get_training_data(self):
        pass

    @abstractmethod
    def get_production_data(self):
        pass

    @abstractmethod
    def transform_production_payload(self):
        pass


