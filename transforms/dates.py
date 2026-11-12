import datetime

def make_date(day: str, month: str, year: str, asDatetime=True):
    '''
    Read a date input and parse it into a datetime or date object
    '''

    datestring = f'{day}/{month}/{year}'
    pattern = '%d/%m/%Y'
    parsed = datetime.datetime.strptime(datestring, pattern)

    return parsed if asDatetime else parsed.date()