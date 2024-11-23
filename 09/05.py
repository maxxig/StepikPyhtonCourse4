import re
class Domain:
    @classmethod
    def check(cls, text):
        match = re.match(r'^(https?:\/\/)?([\da-z-]+)\.{1}([a-z]{2,6})$', text)
        match2 = re.match(r'^[a-zA-Z0-9.%+-]+@([a-zA-Z0-9-]+\.{1}[a-zA-Z]{2,})$', text)
        if match:
            return match.groups()[1] + '.' + match.groups()[2]
        elif match2:
            return match2.groups()[0]
        else:
            return False

    def __init__(self, text=None):
        _domain = self.check(text)
        if not _domain:
            raise DomainException("Недопустимый домен, url или email")
        else:
            self.domain = _domain

    @classmethod
    def from_url(cls, text):
        if not cls.check(text):
            raise DomainException("Недопустимый домен, url или email")
        else:
            return Domain(text)
    @classmethod
    def from_email(cls, text):
        return cls.from_url(text)
    def __str__(self):
        return self.domain


class DomainException(Exception):
    def __init__(self, message):
        super().__init__(message)




