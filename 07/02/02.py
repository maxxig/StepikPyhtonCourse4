from datetime import datetime
class WeatherWarning:
    def  rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')
    def snow(self):
        print('Ожидается снег и усиление ветра')
    def low_temperature(self):
        print('Ожидается сильное понижение температуры')
class WeatherWarningWithDate(WeatherWarning):
    @classmethod
    def print_date(cls, date):
        print(date.strftime('%d.%m.%Y'))
    def rain(self, date):
        self.print_date(date)
        super().rain()
    def snow(self, date):
        self.print_date(date)
        super().snow()
    def low_temperature(self, date):
        self.print_date(date)
        super().low_temperature()
