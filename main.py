import openpyxl, os, sys, itertools
from exelutility import xlsx_cell, calc_value_cell
from util   import twenty4_twelve, getMinute, calc_diff, am_pm_remover, data_extract

dir_src = os.path.dirname(__file__)

REFERENCE_LOCATION = 'ilorin'
REFERENCE_DATA = ''

NUMNER_FILES = 0

def contentExtractor(filename):
    clean_data_no_empty = []
    with open(filename, 'r') as data:
        datacontent = data.read()

    dataLine = datacontent.splitlines()
    for data in dataLine:
        if len(data) == 0:continue
        else:
            clean_data_no_empty.append(data.strip())

    return clean_data_no_empty


def getFileinFolder(dir,list_extn='.txt'):
    '''This method accept folder and file extension as a list object and returns all file in the given folder with specify extension
    This method open needed directory and return  the file and directory name'''
    files = set()
    for p, f, fl in os.walk(dir):
        for file in fl:
            dot_pos = file.find('.')
            exten = file[dot_pos:]
            if exten != list_extn:continue
            else:
                files.add(os.path.join(p, file))
    return files

def calc_location_content(fileList):
    """This function open each file in a given list and return the content in a single list object"""
    bucket = []
    final_bucket = []
    for file in fileList:
        if  REFERENCE_LOCATION.lower() in file.lower():continue
        else:
            content = contentExtractor(file)
            bucket.append(content)
    for item in bucket:
        final_bucket.append(datelocation(item))
    return len(final_bucket), final_bucket

def current_location_file(files):
    file = getReferenceplace(files)
    current_location_content = contentExtractor(file)
    current_location_content = datelocation(current_location_content)
    return current_location_content

def getReferenceplace(files):
    '''determine file of Reference Location'''
    for file in files:
        ext_ = file.find('.')
        filename = file[:ext_]
        if not REFERENCE_LOCATION.lower() in filename.lower():continue
        else:
            return file

def datelocation(listobj):
    '''Dicovering where extraction should commnece'''
    date_collection = []
    for eachline in listobj:
        if eachline[2] != '/':continue
        else:
            date_collection.append(eachline)
    return date_collection

def getPreData(*args):
    '''This function accept list object of form
    ['01/08/2019     05:18     06:34     12:48     16:08     19:03     20:21',........ for any length
    and return list object of form [('01/08/2019', '05:18am', '12:48am', '4:08pm', '7:03pm', '8:21pm'), ('02/08/2019', '05:18am', '12:48am', '4:08pm', '7:03pm', '8:21pm')
    '''
    town_container = []
    for each_town in args[0]:
        words = each_town.split('   ')
        row_date = words[0].strip()
        row_subuh_time = twenty4_twelve(words[1].strip())
        row_Zuhr_time = twenty4_twelve(words[3].strip())
        row_Asr_time = twenty4_twelve(words[4].strip())
        row_Magrib_time = twenty4_twelve(words[5].strip())
        row_Ishai_time = twenty4_twelve(words[6].strip())
        town_container.append(
        (row_date, row_subuh_time, row_Zuhr_time, row_Asr_time, row_Magrib_time, row_Ishai_time))

    return town_container

def getDatavalue(*args):
    '''This method extract data from given list obj and return another list object'''
    data_container = []
    if args[0] == 0:
        datalenght = len(args[1])
    else:
        datalenght = args[0]
    if args[0] != 0:
        data_container.append(getPreData(args[1][0]))
        data_container.append(getPreData(args[1][1]))
        data_container.append(getPreData(args[1][2]))
        data_container.append(getPreData(args[1][3]))
        data_container.append(getPreData(args[1][4]))
        data_container.append(getPreData(args[1][5]))
    else:
        data = getPreData(args[1])
        data_container.extend(data)

    return data_container,  datalenght


def locationExtractor(listobj):
    '''This extract Location from file
    We consume list object and return various type of data'''

    Location = set()
    for line in listobj:
        if not line.startswith('-'):continue
        else:
            if line[3] != 'I':continue
            else:
                word = line.split(' ')
                Location.add(word[2])

    return Location

def ref_calc_place(*args):
    if args[0] < len(args[1]):
        return args[1]
    else:
        return town_data(args[0], args[1])


def town_data(*args):
    """Three parameter will be supply and """

    ref_data = data_extract(REFERENCE_DATA,REFERENCE_DATA)
    kount = 0
    while kount < args[0]:
        if kount == 0:
            next_town = list_unpacking(kount, args[1])
            current_next_town0 = data_extract(REFERENCE_DATA, next_town)
        elif kount == 1:
            next_town = list_unpacking(kount, args[1])
            current_next_town1 = data_extract(REFERENCE_DATA, next_town)
        elif kount == 2:
            next_town = list_unpacking(kount, args[1])
            current_next_town2 = data_extract(REFERENCE_DATA, next_town)
        elif kount == 3:
            next_town = list_unpacking(kount, args[1])
            current_next_town3 = data_extract(REFERENCE_DATA, next_town)
        elif kount == 4:
            next_town = list_unpacking(kount, args[1])
            current_next_town4 = data_extract(REFERENCE_DATA, next_town)
        elif kount == 5:
            next_town = list_unpacking(kount, args[1])
            current_next_town5 = data_extract(REFERENCE_DATA, next_town)

        kount += 1

    return ref_data, current_next_town0, current_next_town1, current_next_town2, current_next_town3, current_next_town4, current_next_town5



def list_unpacking(*args):
    ''' This method is slicing complex List to extract list for one Town alone'''
    next_town = args[1][args[0]]
    return next_town

def list_split(*args):
    daily_prayer = []
    for ref, calc in zip(args[0], args[1]):
        for unit_ref, unit_calc in zip(ref, calc):
            subuh = calc_diff(unit_ref, unit_calc)
            Zuhr = calc_diff(unit_ref, unit_calc)
            Asri = calc_diff(unit_ref, unit_calc)
            Magrib = calc_diff(unit_ref, unit_calc)
            Isha = calc_diff(unit_ref, unit_calc)
        daily_prayer.append([subuh,Zuhr,Asri,Magrib,Isha])


    return daily_prayer, len(daily_prayer)



    # print('what is in k here :',k[1])

    # for ref, cal in zip(args[0], args[1]):
    #     subuh = calc_diff(ref[0], cal[0])
    #     Zuhr = calc_diff(ref[1], cal[1])
    #     Asri = calc_diff(ref[2], cal[2])
    # print(subuh)
    # print(Zuhr)
    # print(Asri)


def explode_calc_place(listobj):
    for place in listobj:
        return place

if __name__ == '__main__':
    files = getFileinFolder(dir_src)
    ref_days_data = current_location_file(files)
    number_files, calc_days_data = calc_location_content(files)

    # print(calc_days_data)
    # print('ilorin : ',ref_days_data)

    ref_location = (locationExtractor(current_location_file(files)))
    ref_data, ref_datalength  = getDatavalue(0,ref_days_data)
    calc_data, calc_datalength  = getDatavalue(number_files, calc_days_data)

    REFERENCE_DATA = ref_data
    Ilorin, town1, town2, town3, town4, town5, town6 = ref_calc_place(calc_datalength,calc_data)
    listobj = list_split(Ilorin, town1)
    calc_value_cell(listobj, 7)
    # getMinute(list_split(Ilorin, town1))
    # getMinute(list_split(Ilorin, town2))
    # getMinute(list_split(Ilorin, town3))
    # getMinute(list_split(Ilorin, town4))
    # getMinute(list_split(Ilorin, town5))
    # getMinute(list_split(Ilorin, town6))
    # getMinute(list_split(Ilorin, Ilorin))

    # print(ref_data)
    xlsx_cell(ref_data)

