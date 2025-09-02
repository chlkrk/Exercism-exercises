def leap_year(year):
    year_divided_4 = year % 4
    year_divided_100 = year % 100
    year_divided_400 = year % 400
    if year_divided_4 == 0 and (year_divided_100 != 0 or year_divided_400 == 0):
        return True
    else:
        return False
