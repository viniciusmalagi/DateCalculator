from enum_date_calculator import Months, KeyOfMonth, KeyOfWeek, YEAR_1900_TO_1999

def month_has_31_days(month:int) -> bool:
    return (month % 2 != 0 and month <= 7) or (month >= 8 and month % 2 == 0)

def get_day_of_week(date:str) -> str:
    day_of_week = ""
    d, m, y = map(int, date.split("/"))
    if y >= 1900 and y <= 2099:
        adjustment = 1 if y >= 2000 else 0
        yy = int(f"{y}"[-2:])
        key_month = KeyOfMonth.__dict__[Months(m).name].value
        count = 0
        for key_y in YEAR_1900_TO_1999:
            if yy in key_y:
                break
            count += 1
        # day + key month + key year - greatest multiple of 7 = day of week
        if count == 0 and adjustment:
            count = 7
        key_day_week = d + key_month + (count - adjustment)
        week = key_day_week - (int(key_day_week / 7) * 7)
        day_of_week = KeyOfWeek(week).name.title()
    return day_of_week


def date_calculator_by_days(date:str, days:int) -> str:
    # Splitting values and converting to int
    d, m, y = map(int, date.split("/"))
    d += days
    m_days = 31
    while d > m_days:
        if m == 2:
            m_days = 29 if m % 4 == 0 else 28
        else:
            m_days = 31 if month_has_31_days(m) else 30
        d -= m_days
        m += 1
        if m > 12:
            y += 1
            m = 1
    return f"{d}/{m}/{y}"

def date_calculator_by_weeks(date: str, weeks:int) -> str:
    return date_calculator_by_days(date, 7 * weeks)

def date_calculator_by_months(date: str, months: int) -> str:
    d, m, y = map(int, date.split("/"))
    m += months
    while(m > 12):
        m -= 12
        y+= 1
        if d == 31:
            d = 31 if month_has_31_days(m) else 30
    return f"{d}/{m}/{y}"

def date_calculator_by_years(date: str, years:int) -> str:
    d, m, y = map(int, date.split("/"))
    y += years
    return f"{d}/{m}/{y}"

def date_calculator(date: str, years:str, months: str, weeks:str, days: str) -> tuple:
    new_date = date
    report = "Is the date"
    if years:
        new_date = date_calculator_by_years(new_date, int(years))
        report += f" {years} Year(s),"
    if months:
        new_date = date_calculator_by_months(new_date, int(months))
        report += f" {months} Month(s),"
    if weeks:
        new_date = date_calculator_by_weeks(new_date, int(weeks))
        report += f" {weeks} Week(s),"
    if days:
        new_date = date_calculator_by_days(new_date, int(days))
        report += f" {days} Day(s),"
    day_of_week = get_day_of_week(new_date)
    return new_date, report, day_of_week
