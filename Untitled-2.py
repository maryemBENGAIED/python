import datetime
def leap_year(year):
    """

    :param year: an integer representing a year
    :return: True if the year is leap and False otherwise
    """
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
min=datetime.MINYEAR
max=datetime.MAXYEAR

def days_in_month(year,month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if (1 <= month <= 12) and (min <= year <= max):
        if month in {1,3,5,7,8,10,12}:
            return 31
        elif (leap_year(year)==True) and (month==2):
            return 29
        elif (leap_year(year)==False) and (month==2):
            return 28
        else:
            return 30
#print("This month has",str(days_in_month(2016,2)),"days")

def is_valid_date(year,month,day):
    """
       Inputs:
         year  - an integer representing the year
         month - an integer representing the month
         day   - an integer representing the day

       Returns:
         True if year-month-day is a valid date and
         False otherwise
       """
    #number of days in that month
    nb_days=days_in_month(year,month)
    if (1<=day<=nb_days) and (1<=month<=12) and (min<=year<=max):
        return True
    else:
        return False
#print(is_valid_date(2017,2,32))

def days_between(year1,month1,day1,year2,month2,day2):
    """
       Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
        """
    date1=datetime.date(year1,month1,day1)
    date2=datetime.date(year2,month2,day2)
    valid_date1=is_valid_date(year1,month1,day1)
    valid_date2=is_valid_date(year2,month2,day2)
    print(date1,date2,valid_date1,valid_date2)
    if (valid_date1==True) and (valid_date2==True):
        if date1<date2==True:
            return date2-date1
        else:
            return 0
    else:
        return 0
print(days_between(2017,1,1,2018,1,2))