class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

# TEST_3:
books = [Book('Программируем на Python', 'Майкл Доусон', 2023), Book('Чистый Python', 'Дэн Бейдер', 2022), Book('Python. Книга рецептов', 'Бизли и Джонс', 2020)]

print(repr(books))

# TEST_4:
books = [
    Book('Python. К вершинам мастерства', 'Лусиану Рамальо', 2022),
    Book('Лёгкий способо выучить Python', 'Зед Шоу', 2019),
    Book('Изучаем Python', 'Эрик Мэтиз', 2017),
    Book('Python. Экспресс курс', 'Наоми Седер', 2019),
    Book('Pandas. Работа с данными', 'Абдрахманов М.И.', 2020),
    Book('Python и анализ данных', 'Уэс Маккини', 2020),
    Book('Грокаем алгоритмы', 'Адитья Бхаргава', 2017),
]

for book in books:
    print(book.__str__(), book.__repr__(), sep='\n', end='\n\n')