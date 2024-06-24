from collections.abc import Sequence

class DNA(Sequence):
    the_dict = {
        "T": "A",
        "A": "T",
        "G": "C",
        "C": "G"
    }
    def __init__(self, chain):
        self._chain = chain
        self._el = [(c, self.the_dict[c]) for c in self._chain]
    def __getitem__(self, item):
        return self._el[item]
    def __len__(self):
        return len(self._el)
    def __repr__(self):
        return self._chain
    def __contains__(self, item):

        return item in self._chain
    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA(self._chain + other._chain)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, DNA):
            return self._chain == other._chain
        else:
            return NotImplemented