class SparseArray:
    def __init__(self, default):
        self.default = default
        self.array = {}
    def __setitem__(self, key, value):
        self.array[key] = value
    def __getitem__(self, item):
        try:
            res = self.array[item]
        except:
            res = self.default
        return res

# TEST_4:
array = SparseArray(None)

for i in range(10000):
    array[i] = 'beegeek'

print(array[0] == array[9999])

# TEST_5:
array = SparseArray(None)

indexes = [516, 3610, 2080, 4131, 1583, 3120, 1591, 4674, 3652, 2632, 1609, 2644, 3677, 1118, 3181, 3695, 2685, 3712,
           644, 4230, 4744, 3219, 660, 4759, 1690, 4252, 4258, 4773, 4777, 1710, 2736, 1717, 1212, 705, 4292, 4809,
           3788, 4302, 4315, 4829, 1246, 737, 3814, 743, 4853, 4342, 3837, 3339, 3343, 3346, 1301, 1818, 1819, 2331,
           1307, 4389, 808, 3371, 2860, 819, 1332, 2870, 3382, 4417, 4419, 2373, 2377, 2389, 1372, 2912, 3425, 4970,
           2923, 4462, 1909, 4473, 4487, 1938, 3475, 918, 2455, 2970, 2458, 3995, 1439, 1955, 2468, 1445, 1965, 4536,
           4544, 1985, 4037, 1478, 969, 4052, 4084, 4089, 506]

for ind in indexes:
    array[ind] = 'Мне больно видеть белый свет, мне лучше в полной темноте'
    print(array[ind])

# TEST_6:
array = SparseArray('Тут ничего нет')

array[1000] = 1000
print(array[999])
print(array[1000])