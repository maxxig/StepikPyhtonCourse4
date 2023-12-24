class Time:
    @staticmethod
    def convert(hour, minute):
        h, m = float, float
        if hour >= 24:
            h = hour % 24
        else:
            h = hour
        if minute >= 60:
            h += minute // 60
            m = minute % 60
        else:
            m = minute
        return (h, m)
    def __init__(self, hour, minute):
        res = Time.convert(hour, minute)
        self.hour = res[0]
        self.minute = res[1]
    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"
    def __add__(self, other):
        if isinstance(other, Time):
            h = self.hour + other.hour
            m = self.minute + other.minute
            res = Time.convert(h, m)
            return Time(res[0], res[1])
        else:
            return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, Time):
            h = self.hour + other.hour
            m = self.minute + other.minute
            res = Time.convert(h, m)
            self.hour = res[0]
            self.minute = res[1]
            return self
        else:
            return NotImplemented


# TEST_3:
time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)



