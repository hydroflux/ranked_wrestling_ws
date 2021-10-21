from pandas import DataFrame


def create_dataframe(stats):
    return DataFrame([stat.__dict__ for stat in stats])


def export_stats(stats):
    dataframe = create_dataframe(stats)