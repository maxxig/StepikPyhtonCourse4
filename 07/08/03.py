import random
class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
    def __repr__(self):
        return f"{self._suit}{self._rank}"

class Deck:
    def __init__(self):
        self._items = []
        for s in ['♣', '♢', '♡', '♠']:
            for r in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self._items.append(Card(s, r))
    def shuffle(self):
        if len(self._items) == 52:
            random.shuffle(self._items)
        else:
            raise ValueError("Перемешивать можно только полную колоду")

    def deal(self):
        if len(self._items)>0:
            return self._items.pop()
        else:
            raise ValueError("Все карты разыграны")
    def __repr__(self):
        return f"Карт в колоде: {len(self._items)}"


# TEST_6:
deck = Deck()

deck.shuffle()

for _ in range(52):
    print(deck.deal())