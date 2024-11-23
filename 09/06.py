class HighScoreTable:
    def __init__(self, value):
        self._max_scores = value
        self.scores = []

    def update(self, value):
        if len(self.scores) < self._max_scores:
            self.scores.append(value)
            self.scores.sort(reverse=True)
        else:
            _tmp = self.scores.copy()
            _tmp.append(value)
            _tmp.sort(reverse=True)
            _tmp = _tmp[:self._max_scores]
            self.scores = _tmp.copy()
            del _tmp
    def reset(self):
        self.scores = []

