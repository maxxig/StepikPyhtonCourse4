import copy
class P:
    def __init__(self, length):
        self.length = length
        self._list = []
        self._tmp_str = ''
    def decorate_just(self, s):
        return s.strip()
    def add(self, string):
        for s in string.split(' '):
            if len(self._tmp_str) + len(s) <= self.length:
                self._tmp_str = self._tmp_str + s + ' '
            else:
                self._list.append(copy.copy(self._tmp_str))
                self._tmp_str = s + ' '
    def end(self):
        if len(self._tmp_str)>0:
            self._list.append(copy.copy(self._tmp_str))
            self._tmp_str = ''
        for l in self._list:
            print(self.decorate_just(l))
        self._list.clear()

class LeftParagraph(P):
    pass
class RightParagraph(P):
    def decorate_just(self, s):
        return s.strip().rjust(self.length)

# TEST_3:
leftparagraph = LeftParagraph(23)

leftparagraph.add('Multiply noise and joy')
leftparagraph.add('Sing songs in a good hour')
leftparagraph.add('Friendship grace and youth')
leftparagraph.add('Our birthday girls')
leftparagraph.end()