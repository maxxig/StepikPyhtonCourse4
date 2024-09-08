from datetime import datetime
class Date:
    def __init__(self, year, month, day):
        self._date = datetime(year, month, day)
    def format(self):
        return self._date.strftime("%m-%d-%Y")
    def iso_format(self):
        return self._date.strftime("%Y-%m-%d")
class USADate(Date):
    pass
class ItalianDate(Date):
    def format(self):
        return self._date.strftime("%d/%m/%Y")

# TEST_4:
dates = [(1988, 2, 28), (2006, 8, 26), (2010, 11, 22), (2021, 9, 13), (1967, 8, 26), (1964, 1, 22), (1983, 12, 7),
         (1967, 11, 5), (1971, 4, 3), (1971, 6, 4), (1986, 9, 14), (2014, 5, 8), (2000, 2, 22), (2005, 7, 5),
         (2018, 5, 10), (1988, 12, 17), (2006, 3, 8), (1993, 9, 4), (1995, 1, 13), (2013, 4, 10), (1998, 12, 25),
         (1996, 4, 23), (1987, 7, 27), (2011, 4, 14), (1970, 2, 11), (1970, 8, 18), (1978, 8, 13), (2000, 8, 22),
         (1982, 1, 13), (1990, 12, 5), (1984, 7, 14), (1987, 3, 28), (1962, 9, 1), (2015, 9, 26), (2020, 12, 10),
         (2008, 11, 1), (1967, 1, 23), (1994, 10, 11), (2018, 3, 4), (1960, 1, 7), (2000, 8, 7), (1962, 12, 9),
         (1982, 2, 18), (2012, 1, 8), (2002, 8, 24), (1990, 2, 1), (1990, 10, 7), (1995, 6, 23), (2022, 11, 5),
         (2004, 6, 9)]

for year, day, month in dates:
    italiandate = ItalianDate(year, day, month)
    print(italiandate.format(), italiandate.iso_format())