import os
from pandas import DataFrame, ExcelWriter

from variables.export import start_row, header

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
        startrow=start_row,
        header=False,
        index=False
    )
    return writer, file_name


def count_columns(dataframe):
    return len(dataframe.columns)


def access_last_column(dataframe):
    return chr(ord("@") + (count_columns(dataframe)))


def access_last_row(dataframe):
    return len(dataframe.index) + start_row


def set_page_format(dataframe, worksheet):
    worksheet.set_landscape()
    worksheet.set_paper(5)
    worksheet.set_margins(left=0.25, right=0.25, top=0.75, bottom=0.75)
    worksheet.hide_gridlines(2)
    worksheet.freeze_panes(f'A{start_row + 1}')
    worksheet.autofilter(f'A2:{access_last_column(dataframe)}{access_last_row(dataframe) + 1}')


def set_title_row_format(dataframe, worksheet):
    worksheet.set_row(0, header["height"])
    worksheet.merge_range(f'A1:{access_last_column(dataframe)}1', '', header['font'])


def add_title_row(file_name, dataframe, worksheet):
    set_title_row_format(dataframe, worksheet)


def add_headers(dataframe, worksheet):
    pass


def set_border(dataframe, worksheet):
    pass


def add_content(file_name, dataframe, worksheet):
    add_title_row(file_name, dataframe, worksheet)
    add_headers(dataframe, worksheet)
    set_border(dataframe, worksheet)


def create_xlsx_document(division, writer, file_name, dataframe):
    worksheet = writer.sheets[division.division_abbreviation]
    set_page_format(dataframe, worksheet)
    add_content(file_name, dataframe, worksheet)


def export_stats(season, division, stats):
    os.chdir(target_directory)
    dataframe = create_dataframe(stats)
    writer, file_name = create_stats_object(season, division, dataframe)
    create_xlsx_document(division, writer, file_name, dataframe)
