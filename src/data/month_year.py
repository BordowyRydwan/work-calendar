import datetime

_day = datetime.datetime.now().day
_month = datetime.datetime.now().month
_year = datetime.datetime.now().year

_base_day = _day
_base_month = _month
_base_year = _year


def month_back():
    global _month, _year
    year_break = _month == 1

    if year_break:
        _year -= 1
        _month = 12
    else:
        _month -= 1


def month_forward():
    global _month, _year
    year_break = _month == 12

    if year_break:
        _year += 1
        _month = 1
    else:
        _month += 1


def is_day_current():
    return _day == _base_day and is_month_current()


def is_month_current():
    return _base_month == _month and _base_year == _year


def set_day(day):
    _day = day
