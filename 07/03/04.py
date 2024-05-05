class TitledText(str):
    def __new__(cls, content, text_title):
        instance = str.__new__(cls, content)
        instance._text_title = text_title
        return instance
    def title(self):
        return self._text_title

