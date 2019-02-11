from project.data_science.s2_target_generators.abc_target_gen import ABcTargetGen


class TargetGenIdentity(ABcTargetGen):

    @staticmethod
    def generate_target(data=None):
        col='y'
        y=data[col]
        online_data=data[[x for x in data.columns if x!=col]]
        return online_data,y



