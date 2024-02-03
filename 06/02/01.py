class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        yield from reversed(self.sequence)
    def __len__(self):
        return len(self.sequence)
    def __getitem__(self, key):
        if not isinstance(key, int):
            pass
        else:
            return list(reversed(self.sequence))[key]

# TEST_4:
reversed_numbers = ReversedSequence((1, 2, 3, 4, 5))

for num in reversed_numbers:
    print(num)

# TEST_5:
reversed_chars = ReversedSequence('abcde')

for char in reversed_chars:
    print(char)

# TEST_6:
reversed_chars = ReversedSequence('abcdefghijklmnopqrstuvwxyz')

print(reversed_chars[0], reversed_chars[7], reversed_chars[11], reversed_chars[25])

# TEST_7:
reversed_list = ReversedSequence(['Gvido', 'Elon', 'Gates', 'Jobs', 'Zuckerberg'])

print(*reversed(reversed_list))