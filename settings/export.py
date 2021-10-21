import os
from pandas import DataFrame, ExcelWriter

from variables.export import start_row, title_format, header_format, border_format, last_column, xlsx_columns

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
    writer = create_excel_writer(file_name)
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


def access_last_row(dataframe):
    return len(dataframe.index) + start_row


def set_font_formats(workbook):
    return {
        'title': workbook.add_format(title_format['font']),
        'header': workbook.add_format(header_format['font']),
        'border': workbook.add_format(border_format['border']),
    }


def set_page_format(dataframe, worksheet):
    worksheet.set_landscape()
    worksheet.set_paper(5)
    worksheet.set_margins(left=0.25, right=0.25, top=0.75, bottom=0.75)
    worksheet.hide_gridlines(2)
    worksheet.freeze_panes(f'A{start_row + 1}')
    worksheet.autofilter(f'A{start_row}:{last_column}{access_last_row(dataframe) + 1}')


def add_title_row(file_name, worksheet, font_formats):
    worksheet.set_row(0, title_format["height"])
    worksheet.merge_range(f'A1:{last_column}1', file_name, font_formats['title'])


def add_headers(dataframe, worksheet, font_formats):
    for index in range(count_columns(dataframe)):
        name = dataframe.columns[index]
        position = xlsx_columns[index]
        worksheet.merge_range(
            f'{position}2:{position}3',
            name,
            font_formats['header']
        )


def access_worksheet_range(dataframe):
    return f'A{start_row}:{last_column}{access_last_row(dataframe)}'


def set_border(dataframe, worksheet, font_formats):
    worksheet_range = access_worksheet_range(dataframe)
    border_format['1']['format'] = font_formats['border']
    border_format['2']['format'] = font_formats['border']
    worksheet.conditional_format(worksheet_range, border_format['1'])
    worksheet.conditional_format(worksheet_range, border_format['2'])


def add_content(file_name, dataframe, worksheet, font_formats):
    add_title_row(file_name, worksheet, font_formats)
    add_headers(dataframe, worksheet, font_formats)
    set_border(dataframe, worksheet, font_formats)


def create_xlsx_document(division, writer, file_name, dataframe):
    workbook = writer.book
    worksheet = writer.sheets[division.division_abbreviation]
    font_formats = set_font_formats(workbook)
    set_page_format(dataframe, worksheet)
    add_content(file_name, dataframe, worksheet, font_formats)
    return workbook


def export_stats(season, division, stats):
    os.chdir(target_directory)
    dataframe = create_dataframe(stats)
    writer, file_name = create_stats_object(season, division, dataframe)
    workbook = create_xlsx_document(division, writer, file_name, dataframe)
    workbook.close()
