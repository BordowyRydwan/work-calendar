import datetime

month = datetime.datetime.now().month
year = datetime.datetime.now().year

base_month = month
base_year = year


def month_back():
    global month, year
    year_break = month == 1

    if year_break:
        year -= 1
        month = 12
    else:
        month -= 1


def month_forward():
    global month, year
    year_break = month == 12

    if year_break:
        year += 1
        month = 1
    else:
        month += 1


def is_month_current():
    return base_month == month and base_year == year
