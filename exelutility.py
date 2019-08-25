import openpyxl as exel
import os
dir_src = os.path.dirname(__file__)

def create_workbook():
    # A copy of workbook and one single worksheet is produce to the calling functions

    wkbook = exel.Workbook()
    wsheet = wkbook.active
    return wkbook, wsheet

def xlxsfield_creator(current_sheet, cell_spacer=0):
    # wkbook, current_sheet = create_workbook()
    current_sheet.cell(row=2, column=4+cell_spacer).value = 'Town'
    current_sheet.cell(row=2, column=5+cell_spacer).value = 'Ilorin'
    current_sheet.cell(row=3, column=1 + cell_spacer).value = 'Date'
    current_sheet.cell(row=3, column=2 + cell_spacer).value  = 'Fajr & Shuruq'
    current_sheet.cell(row=3, column=3 + cell_spacer).value = 'Zurh'
    current_sheet.cell(row=3, column=4 + cell_spacer).value = 'Asr'
    current_sheet.cell(row=3, column=5 + cell_spacer).value = 'Magrib'
    current_sheet.cell(row=3, column=6 + cell_spacer).value = 'Isha'


def xlsx_cell(listobj, cell_spacer=0, ):
    wkbook, current_sheet = create_workbook()
    xlsx_row = len(listobj)
    num_row = 0
    while num_row < xlsx_row:
        current_sheet.cell(row=num_row + 4, column=1+cell_spacer).value = listobj[num_row][0]
        current_sheet.cell(row=num_row + 4, column=2+cell_spacer).value = listobj[num_row][1]
        current_sheet.cell(row=num_row + 4, column=3+cell_spacer).value = listobj[num_row][2]
        current_sheet.cell(row=num_row + 4, column=4+cell_spacer).value = listobj[num_row][3]
        current_sheet.cell(row=num_row + 4, column=5+cell_spacer).value = listobj[num_row][4]
        current_sheet.cell(row=num_row + 4, column=6+cell_spacer).value = listobj[num_row][5]
        num_row += 1
    xlxsfield_creator(current_sheet,cell_spacer)

    wkbook.save('data.xlsx')


def calcute_place(listobj):
    wkbook, current_sheet = create_workbook()
    num_town = len(listobj)
    num_row = len(listobj[0])
    town = 0
    town_column = 7
    town_row = 0
    while town < num_town:
        while town_row < num_row:
            current_sheet.cell(row=town_row + 4, column=town_column+1).value = listobj[num_row][0]
            current_sheet.cell(row=town_row + 4, column=town_column+2).value = listobj[num_row][1]
            current_sheet.cell(row=town_row + 4, column=town_column+3).value = listobj[num_row][2]
            current_sheet.cell(row=town_row + 4, column=town_column+4).value = listobj[num_row][3]
            current_sheet.cell(row=town_row + 4, column=town_column+5).value = listobj[num_row][4]
            current_sheet.cell(row=town_row + 4, column=town_column+6).value = listobj[num_row][5]
            town_row += 1
        town_column += town_column
        town += 1
        xlxsfield_creator(current_sheet)

        wkbook.save('data.xlsx')

# xlxsfield_creator('ee', 'wer')



