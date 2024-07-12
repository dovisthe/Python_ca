def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def get_leap_years(start_year, end_year):
    leap_years = []
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_years.append(year)
    return leap_years