import os
from pandas import DataFrame, ExcelWriter

from settings.settings import target_directory


def build_file_name(season, division):
    return f'{division}{season.year}'


def create_dataframe(stats):
    return DataFrame([stat.__dict__ for stat in stats])


def create_excel_writer(file_name):
    return ExcelWriter(
        file_name,
        engine='xlsxwriter',
        datetime_format='mm/dd/yyyy',
        date_format='mm/dd/yyyy')


def create_stats_object(season, division, dataframe):
    file_name = build_file_name(season, division)
    writer = create_dataframe(file_name)
    dataframe.to_excel(
        writer,
        sheet_name=division.division_abbreviation,
        # startrow=,
        header=False,
        index=False
    )
    return writer


def set_page_format(worksheet):
    pass


def format_xlsx_document(workbook, worksheet):
    pass


def create_xlsx_document(division, writer, dataframe):
    workbook = writer.book
    worksheet = writer.sheets[division.division_abbreviation]


def export_stats(season, division, stats):
    os.chdir(target_directory)
    dataframe = create_dataframe(stats)
    writer = create_stats_object(season, division, dataframe)
    create_xlsx_document(division, writer, dataframe)
