from datetime import timedelta
from enum import Enum
class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, today, weekday: Weekday, considering_today =False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today
    def date(self):
        _res = self.today + timedelta(days=self.days_until())
        return _res
    def days_until(self):
        _res = 0
        day_of_date = self.today.weekday()
        if self.considering_today and Weekday(day_of_date) == self.weekday:
            return 0
        else:
            for i in range(7):
                day_of_date += 1
                if day_of_date > 6:
                    day_of_date = 0
                _res += 1
                if Weekday(day_of_date) == self.weekday:
                    return _res


# TEST_7:
from datetime import date, timedelta

today = date(2023, 4, 23)

for _ in range(7):
    today += timedelta(days=1)
    for weekday in Weekday:
        next_date = NextDate(today, weekday, True)
        print(f'Today = {today} {Weekday(today.weekday()).name}, next {weekday.name} = {next_date.date()}')
        print(f'Days until = {next_date.days_until()}')