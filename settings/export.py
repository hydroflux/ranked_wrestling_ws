import os
from pandas import DataFrame

from settings.settings import target_directory


def build_file_name(season, division):
    return f'{division}{season.year}'


def create_dataframe(stats):
    return DataFrame([stat.__dict__ for stat in stats])


def export_stats(season, division, stats):
    os.chdir(target_directory)
    file_name = build_file_name(season, division)
    dataframe = create_dataframe(stats)