import math
class SuperInt(int):
    def repeat(self, n = 2):
        # print(str(abs(self))*2)
        # return SuperInt(int(str(self) + str(abs(self)) * (n-1)))
        return SuperInt(str(self) * n)
    def to_bin(self):
        return format(self,'b')
    def next(self):
        return SuperInt(self + 1)
    def prev(self):
        return SuperInt(self - 1)
    def __iter__(self):
        return map(lambda x: SuperInt(int(x)), str(abs(self)))

superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))