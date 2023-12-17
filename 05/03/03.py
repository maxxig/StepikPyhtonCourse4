from functools import total_ordering
@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month
    def __str__(self):
        return f'{self.year}-{self.month}'
    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple) and len(other) == 2:
            return self.year == other[0] and self.month == other[1]
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return self.year < other.year or (self.year == other.year and self.month < other.month)
        elif isinstance(other, tuple) and len(other) == 2:
            return self.year < other[0] or ( self.year == other[0] and self.month < other[1])
        else:
            return NotImplemented

month = Month(2023, 4)
not_supported = ['04.2023', 4.0, 2023, True, {2023: 4}, {4, 2023}, False, (2023, 4, 'dont know')]
for obj in not_supported:
    print(month == obj)


