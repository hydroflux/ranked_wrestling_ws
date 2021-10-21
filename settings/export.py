import os
from pandas import DataFrame, ExcelWriter

from settings.settings import target_directory


def build_file_name(season, division):
    return f'{division}{season.year}'


def create_dataframe(stats):
    return DataFrame([stat.__dict__ for stat in stats])


def create_excel_writer(output_file):
    return ExcelWriter(
        output_file,
        engine='xlsxwriter',
        datetime_format='mm/dd/yyyy',
        date_format='mm/dd/yyyy')


def create_stats_object(target_directory, writer, dataframe):
    pass


def create_xlsx_document(target_directory, file_name, dataframe):
    pass


def export_stats(season, division, stats):
    os.chdir(target_directory)
    file_name = build_file_name(season, division)
    dataframe = create_dataframe(stats)
    writer = create_xlsx_document(target_directory, file_name, dataframe)