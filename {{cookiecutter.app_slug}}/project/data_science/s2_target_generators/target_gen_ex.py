"""
implementation examples of step 2 : generation of the target variable
"""

from project.data_science.s2_target_generators.abc_target_gen import ABcTargetGen


class TargetGenSimple(ABcTargetGen):
    """
    class for generate x and y
    """

    @staticmethod
    def generate_target(data=None):
        col='y'
        y=data[col]
        online_data=data[[x for x in data.columns if x!=col]]
        return online_data,y


class TargetGenTimeSeries(ABcTargetGen):
    """
    class for generate x and y
    """

    @staticmethod
    def generate_target(data=None):
        col='y'
        y=data[col]
        online_data=data[[x for x in data.columns if x!=col]]
        return online_data,y


