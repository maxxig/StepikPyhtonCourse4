class Filter:
    def __init__(self, predicate = bool):
        self.predicate = predicate
    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))

# TEST_6:
empty_elements = Filter(lambda x: not x)

sequence = [(1, 2, 3), [], set(), 'Beegeek', {}, {1: '12'}, False, True, '', [2023, 4]]
print(empty_elements(sequence))