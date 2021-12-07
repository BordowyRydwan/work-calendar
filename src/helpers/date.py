from data.date import base, calendarView, selected
from data.events import event


def month_back():
    year_break = calendarView.month == 1

    if year_break:
        calendarView.year -= 1
        calendarView.month = 12
    else:
        calendarView.month -= 1

    event.change_month()


def month_forward():
    year_break = calendarView.month == 12

    if year_break:
        calendarView.year += 1
        calendarView.month = 1
    else:
        calendarView.month += 1

    event.change_month()


def is_day_current():
    return calendarView.day == base.day and is_month_current()


def is_month_current():
    return base.month == calendarView.month and base.year == calendarView.year


def parse_to_file_data():
    return {
        'directory': f'{selected.year}-{selected.month}',
        'fileName': f'{selected.day}.txt'
    }


def month_dir_for_calendar_view():
    return f'{calendarView.year}-{calendarView.month}'


def set_day(day):
    selected.day = day
    selected.month = calendarView.month
    selected.year = calendarView.year
    event.change_date(day)
