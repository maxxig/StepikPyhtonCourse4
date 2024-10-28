class Item:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    def __repr__(self):
        return f"{self._name}, {self._price}$"

class ShoppingCart:
    def __init__(self, item = []):
        self._items = item
    def add(self, item):
        self._items.append(item)

    def total(self):
        return sum(map(lambda i: i._price, self._items))
    def remove(self, name):
        for item in self._items:
            if item._name == name:
                self._items.remove(item)
    def __repr__(self):
        return "\n".join(map(lambda i: str(i), self._items))


# TEST_5:
shopping_cart = ShoppingCart()
print(shopping_cart)