from collections import UserDict
class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if len(list(filter(lambda x: x == value,self.data.values())))>0:
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        self.data.__setitem__(key, value)





# TEST_3:
from datetime import date
from itertools import cycle

names = ['Измаил', 'Рюрик', 'Фортунат', 'Сила', 'Ирина', 'Оксана', 'Ипатий', 'Регина', 'Никифор', 'Валерия', 'Эмилия',
         'Порфирий', 'Христофор', 'Герман', 'Иванна', 'Елизар', 'Рубен', 'Сидор', 'Демьян', 'Прохор', 'Элеонора',
         'Милий', 'Марфа', 'Любомир', 'Пелагея', 'Дарья', 'Иосиф', 'Феврония', 'Андроник', 'Ростислав', 'Фаина', 'Боян',
         'Ульяна', 'Николай', 'Григорий', 'Лора', 'Антонина', 'Аггей', 'Бронислав', 'Олимпиада', 'Александра',
         'Евпраксия', 'Ким', 'Еремей', 'Пимен', 'Казимир', 'Фотий', 'Любим', 'Майя', 'Поликарп', 'Клавдия', 'Филипп',
         'Павел', 'Ангелина', 'Станислав', 'Раиса', 'Ольга', 'Назар', 'Добромысл', 'Агата', 'Ладислав', 'Ия', 'Наина',
         'Юлиан', 'Анастасия', 'Акулина', 'Иван', 'Евсей', 'Евдоким', 'Галина', 'Владислав', 'Синклитикия', 'Ираида',
         'Ратибор', 'Юлий', 'Стоян', 'Глафира', 'Панкратий', 'Кира', 'Мстислав', 'Алевтина', 'Виктория', 'Людмила',
         'Октябрина', 'Прасковья', 'Радислав', 'Влас', 'Анжела', 'Ксения']

birth_dates = [date(2018, 2, 3), date(2006, 1, 25), date(1981, 12, 27), date(2005, 5, 26), date(1977, 9, 3),
               date(2021, 4, 26), date(2014, 11, 10), date(2004, 2, 5), date(2000, 10, 9), date(2022, 7, 14),
               date(1974, 6, 2), date(1978, 1, 6), date(2018, 9, 23), date(2001, 8, 1), date(1999, 3, 11),
               date(1984, 7, 7), date(1995, 2, 15), date(1986, 3, 17), date(2009, 2, 16), date(2010, 4, 11)]

birthdaydict = BirthdayDict()

for name, birth_date in zip(names, cycle(birth_dates)):
    birthdaydict[name] = birth_date