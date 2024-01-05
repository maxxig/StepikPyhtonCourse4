class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, name)[0].upper() + object.__getattribute__(self, name)[1:]
        # return self.__dict__[name]
        return object.__getattribute__(self, name)

# TEST_4:
items = [
    Item('Обручальное Кольцо', 49000, 7),
    Item('Мобильный Телефон', 110000, 200),
    Item('Ноутбук', 150000, 2000),
    Item('Ручка Паркер', 37000, 20),
    Item('Статуэтка Оскар', 28000, 4000),
    Item('Наушники', 11000, 150),
    Item('Гитара', 32000, 1500),
    Item('Золотая Монета', 140000, 8),
    Item('Фотоаппарат', 79000, 720),
    Item('Лимитированные Кроссовки', 80000, 300)
]

for item in items:
    print(item.name, item.total)
