class Wordplay:
    def __init__(self, words = []):
        self.words = words.copy()
    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)
    def words_with_length(self, n):
        return [i for i in self.words if len(i) == n]

    def only(self, *args):
        res = []
        for word in self.words:
            can_add = True
            for w in word:
                if w not in args:
                    can_add = False
            if can_add:
                res.append(word)
        return res
    def avoid(self, *args):
        res = []
        for w in self.words:
            is_found = False
            for a in args:
                if a in w:
                    is_found = True
                    continue
            if not is_found and w not in res:
                res.append(w)
        return res


wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.words)
wordplay.add_word('stepik')
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)