class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        # self.name = value
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        # del self.name
        super().__delattr__(name)

# TEST_4:
obj = Logger()

excluded = ['explain', 'much', 'determine', 'response', 'realize', 'wait', 'television', 'million', 'think', 'water',
            'purpose', 'treat', 'both', 'land', 'condition', 'mission', 'air', 'public', 'cultural', 'ok', 'ever',
            'run', 'institution', 'smile', 'industry', 'person', 'leave', 'watch', 'tell', 'while', 'total',
            'interview', 'whom', 'staff', 'technology', 'successful', 'measure', 'country', 'let', 'every', 'design',
            'control', 'realize', 'rather', 'citizen', 'food', 'return', 'pass', 'person', 'week']

for item in excluded:
    try:
        delattr(obj, item)
    except (KeyError, AttributeError):
        print('Класс', obj.__class__.__name__, 'не имеет атрибута', item)
