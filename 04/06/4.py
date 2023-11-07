class Color:
    def __init__(self, hc):
        self.hexcode = hc
    @property
    def hexcode(self):
        return '{:02x}{:02x}{:02x}'.format(self.r, self.g, self.b).upper()

    @hexcode.setter
    def hexcode(self, hc):
        self.r = int(hc[:2], 16)
        self.g = int(hc[2:4], 16)
        self.b = int(hc[4:], 16)

hexcodes = ['FC5A5E', '13AABE', '851149', 'AAAAAA', 'FFFFFF', 'B6A1D8', 'ABCDEF', 'FEDCBA', '123456', '999999']
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f'Цвет № {count}')
    print(color.hexcode)
    print(color.r, color.g, color.b, sep='\n')
    print()
    count += 1