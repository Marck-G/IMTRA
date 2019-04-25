import datetime



def dir(d, format = 'yyyy/MM/dd-MM-yy', sys_date=False):
    """
    Generate a path string with the date and the format
    :param d: date to make the tree dir
    :param format: format of the tree dir
    :return: string with the tree dir
    """
    split_regex = '/'
    if ':' in format: split_regex = ':'
    split = format.split(split_regex)
    # parse the date
    date = datetime.datetime.strptime(str(d), "%Y:%m:%d %H:%M:%S") \
        if str(d).index('.') == -1 else datetime.datetime.strptime(str(d), "%Y-%m-%d %H:%M:%S.%f")
    string = ''
    for el in split:
        # split any subformat
        if '-' in el:
            tmp_split = el.split('-')
            str_el = ''
            for index,i in enumerate(tmp_split):
                str_el = str_el + replace(i, date)
                if index < 2:
                    str_el = str_el + '-'
            string = string + '/' + str_el
        else:
            string = string + '/' + replace(el, date)
    return string


def replace(data, date):
    # year testing
    if 'yyyy' in data:
        return str(date.year)
    if 'yy' in data:
        year = date.year
        return str(year)[2:]
    # month testing
    if 'MM' in data:
        month = str(date.month)
        return month if len(month) == 2 else '0' + month
    # day testing
    if 'dd' in data:
        day = str(date.day)
        return day if len(day) == 2 else '0' + day

