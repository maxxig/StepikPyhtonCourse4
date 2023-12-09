from functools import singledispatch
from datetime import date, timedelta

def get_days_in_month(month, year):
    # Returns the number of days in a given month and year
    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29  # Leap year
        else:
            return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:
        return 31
def current_age(birth_date, current_date):
    # Calculation
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust for negative differences
    if days < 0:
        months -= 1
        days += get_days_in_month(birth_date.month, birth_date.year)
    if months < 0:
        years -= 1
        months += 12

    return years

class BirthInfo:
    def __init__(self, birth_date):
        self.birth_date = BirthInfo.init(birth_date)
    @singledispatch
    @staticmethod
    def init(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    @init.register(date)
    @staticmethod
    def init_date(birth_date):
        return birth_date

    @init.register(str)
    @staticmethod
    def init_date(birth_date):
        res = None
        try:
            res = date.fromisoformat(birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')
        return res

    @init.register(tuple)
    @init.register(list)
    @staticmethod
    def init_tuple_list(birth_date):
        return date(birth_date[0], birth_date[1], birth_date[2])

    @property
    def age(self):
        return current_age(self.birth_date, date.today())


# TEST_7:
birth_dates = ['20200918', '2020-0918', '202009-18', ' 2020-09-18 ', '2020-9-18']

for birth_date in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date)
    except TypeError as e:
        print(e)


