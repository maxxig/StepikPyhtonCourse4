class HourClock:
    @classmethod
    def check_hours(cls, hours):
        if type(hours) != int or not 1 <= hours <= 12:
            raise ValueError('Некорректное время')
        return True
    def __init__(self, hours):
        if self.check_hours(hours):
            self._hours = hours

    def set_hours(self, hours):
        if self.check_hours(hours):
            self._hours = hours

    def get_hours(self):
        return self._hours

    hours = property(get_hours, fset=set_hours)

# TEST_4:
try:
    HourClock(0)
except ValueError as e:
    print(e)

# TEST_5:
try:
    HourClock('ten o`clock')
except ValueError as e:
    print(e)

# TEST_6:
time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)

# TEST_7:
time = HourClock(1)
print(hasattr(HourClock, 'hours'))