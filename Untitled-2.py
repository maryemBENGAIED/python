import datetime


def leap_year(year):
    """

    :param year: an integer representing a year
    :return: True if the year is leap and False otherwise
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    """

    :type month: int
    :type year: int
    :rtype: int
    :param year: n integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
    :param month: an integer between 1 and 12 representing the month
    :return: The number of days in the input month.
    """

    min: int = datetime.MINYEAR
    max: int = datetime.MAXYEAR
    if (1 <= month <= 12) and (min <= year <= max):
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif (leap_year(year) == True) and (month == 2):
            return 29
        elif (leap_year(year) == False) and (month == 2):
            return 28
        else:
            return 30
    else:
        return 0


print(days_in_month(1, 1))


def is_valid_date(year: int, month: int, day: int) -> bool:
    """

    :type day: int
    :type month: int
    :type year: int
    :rtype: bool
    :param year: an integer representing the year
    :param month: an integer representing the month
    :param day: an integer representing the day
    :return: True if year-month-day is a valid date and
         False otherwise
    """
    # number of days in this month
    nb_days: int = days_in_month(year, month)
    min: int = datetime.MINYEAR
    max: int = datetime.MAXYEAR
    if (1 <= day <= nb_days) and (1 <= month <= 12) and (min <= year <= max):
        return True
    elif year == 0:
        return False
    else:
        return False


print(is_valid_date(0, 1, 1))


def days_between(year1, month1, day1, year2, month2, day2) -> int:
    """

    :rtype: int
    :type day2: int
    :type month2: int
    :type year2: int
    :type day1: int
    :type year1: int
    :type month1: int
    :param year1: an integer representing the year of the first date
    :param month1: an integer representing the month of the first date
    :param day1: an integer representing the day of the first date
    :param year2: an integer representing the year of the second date
    :param month2: an integer representing the month of the second date
    :param day2: an integer representing the day of the second date
    :return: The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    valid_date1 = is_valid_date(year1, month1, day1)
    valid_date2 = is_valid_date(year2, month2, day2)

    if (valid_date1 == True) and (valid_date2 == True):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date1 < date2:
            difference = date2 - date1
            return difference.days
        else:
            return 0
    else:
        return 0


print(days_between(20000, 1, 1, 2047, 8, 2))


def age_in_days(year, month, day) -> int:
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
      :rtype: int
      :type day: int
      :type month: int
      :type year: int

    """
    todays_date = datetime.date.today()
    print(todays_date)
    day2: int = todays_date.day
    month2: int = todays_date.month
    year2: int = todays_date.year
    valid_date = is_valid_date(year, month, day)
    if valid_date == True:
        return days_between(year, month, day, year2, month2, day2)
    else:
        return 0


print(age_in_days(2017, 1, 1))
