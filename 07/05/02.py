from abc import ABC, abstractmethod
class ChessPiece(ABC):
    alphabet_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
    @abstractmethod
    def can_move(self, horizontal, vertical):
        pass

class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        cur_x, cur_y = self.alphabet_to_number[self.horizontal], self.alphabet_to_number[self.vertical]
        m_hc, m_vr = self.alphabet_to_number[horizontal], self.alphabet_to_number[vertical]
        if (abs(cur_x - m_hc) * abs(cur_y - m_vr)) <= 1 and (abs(cur_x - m_hc) == 1  or abs(cur_y - m_vr) == 1):
            if m_hc >= 1 and m_hc <= 8 and m_vr >= 1 and m_vr <= 8:
                return True
        return False
class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        cur_x, cur_y = self.alphabet_to_number[self.horizontal], self.alphabet_to_number[self.vertical]
        m_hc, m_vr = self.alphabet_to_number[horizontal], self.alphabet_to_number[vertical]
        if (abs(cur_x - m_hc) * abs(cur_y - m_vr)) == 2:
            if m_hc >= 1 and m_hc <= 8 and m_vr >= 1 and m_vr <= 8:
                return True
        return False

# TEST_8:
knights = [Knight(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for knight in knights:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if knight.can_move(horizontal, vertical):
                print(f'Knight({knight.horizontal}{knight.vertical})', f'{horizontal}{vertical}',
                      knight.can_move(horizontal, vertical))
