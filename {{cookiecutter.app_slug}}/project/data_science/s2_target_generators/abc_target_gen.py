from abc import ABC, abstractmethod


class ABcTargetGen(ABC):
    """
    Abstract Base Class (ABC) for target and model features generation
    """


    @abstractmethod
    def generate_target(self,data=None):
        col='y'
        y=data[col]
        online_data=data[[x for x in data.columns if x!=col]]
        return online_data,y



