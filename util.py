MINUTES_HOUR = 60

def twenty4_twelve(clock24):
    '''Converting 24 hours clock interval to 12 hours clock interval
    example given 15:45
    it will return 3:45pm
    '''
    # print('clock24 before any processing is ',clock24)
    if len(clock24) != 5:pass
    else:
        pre_digit = clock24[:2] # Slice out the first two digit
        if int(pre_digit) == 12:
            return (str(pre_digit) + clock24[2:]+ 'pm')
        elif int(pre_digit) < 12:
            return (str(pre_digit) + clock24[2:] +'am')
        else:
            pre_digit = int(pre_digit) % 12
            return ('0' + str(pre_digit) + clock24[2:] +'pm')


def am_pm_remover(current_time):
    ''' This remove trailing 'am' or 'pm' '''
    # print('what is the current status of in am_pm_function current_time',current_time)
    sentry = len(current_time)
    if  sentry == 7:
        colon_pos = current_time.find(':')
        return current_time[:colon_pos+3]
    elif sentry < 7:
        current_time = '0' + current_time
        colon_pos = current_time.find(':')
        return current_time[:colon_pos + 3]


def hours_minutes(current_time):
    '''Given time is convert from 'HH:MM'to equivalent Minutes'''
    if int(current_time[0]) == 0:
        current_time = current_time[1:]
        clock_hours = int(current_time[:1])
        clock_minutes = int(current_time[2:4])
        total_minutes = (clock_hours * MINUTES_HOUR) + clock_minutes
        return total_minutes
    elif int(current_time[0]) == 1:
        clock_minutes = int(current_time[3:5])
        clock_hours = int(current_time[:2])
        return (MINUTES_HOUR * clock_hours) + clock_minutes

def calc_diff(ref_place, calc_place):
    return calc_place - ref_place



def getMinute(*args):
    all_days = []
    # print('tell me this : ',len(args[0][0]))
    for dailytime in args[0][0]:
        subuh = dailytime[0]
        Zurh = dailytime[1]
        Asri = dailytime[2]
        Magrib = dailytime[3]
        ISha = dailytime[4]
        all_days.append(subuh)
        all_days.append(Zurh)
        all_days.append(Asri)
        all_days.append(Magrib)
        all_days.append(ISha)
    print(all_days)


# def calc_time_adjust(reference_place, other_place):
#     ''' This Method calcuate time difference between two place and return Minutes of dirrefent
#     Usage
#     calc_time_adjust('HH:MM', 'HH:MM)'''
#
#     reference_place = twenty4_twelve(reference_place)
#     other_place = twenty4_twelve(other_place)
#     reference_place = hours_minutes(reference_place)
#     other_place = hours_minutes(other_place)
#
#     return (int(reference_place) - int(other_place))

def time_in_minutes(*args):
    '''This function consume time in format 05:00pm and return time in minutes equivalent
    '''
    town_minute = [] # This hold time in minutes for each prayer daily
    ref_town_data = args[0][0][0]
    # ref_town_name = args[0][0][1]
    other_location_data = args[1][0]
    other_location_name = args[1][1]

    for date_ref, date_calc in zip(ref_town_data, other_location_data):
        # Confirming that the date match up before the need house chore below
        if date_ref[0] == date_calc[0]:  # checking for Date matchup
            # Taking care of time of format 05:00am, by removing the trail 'am' or 'pm'
            sentry = date_ref[1][0]
            if int(sentry) == 0:
                town_minute.append(
                    [hours_minutes(am_pm_remover(date_calc[1][1:])), hours_minutes(am_pm_remover(date_calc[2][:])),
                     hours_minutes(am_pm_remover(date_calc[3][1:])), hours_minutes(am_pm_remover(date_calc[4][1:])),
                     hours_minutes(am_pm_remover(date_calc[5][1:]))])

    return [town_minute,other_location_name]