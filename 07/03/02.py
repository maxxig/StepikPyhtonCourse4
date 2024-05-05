class LowerString(str):
    def __new__(cls, obj=''):
        return super().__new__(cls, str(obj).lower())

# TEST_5:
print(LowerString())

# TEST_6:
lowerstring = LowerString()
print(type(lowerstring))