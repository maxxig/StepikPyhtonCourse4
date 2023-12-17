from functools import total_ordering
@total_ordering
class Version:
    def __init__(self, version):
        v = version.split('.')
        self.version = []
        self.version.append(v[0])
        self.version.append(v[1] if len(v) >= 2 else 0)
        self.version.append(v[2] if len(v) == 3 else 0)

    def __repr__(self):
        return f"Version('{self.version[0]}.{self.version[1]}.{self.version[2]}')"
    def __str__(self):
        return f"{self.version[0]}.{self.version[1]}.{self.version[2]}"

    def __eq__(self, other):
        if isinstance(other, Version):
            self_version = int(f'{self.version[0]}{self.version[1]}{self.version[2]}')
            other_version = int(f'{other.version[0]}{other.version[1]}{other.version[2]}')
            return self_version  == other_version
        else:
            return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Version):
            for i in range(3):
                if int(self.version[i]) < int(other.version[i]):
                    return int(self.version[i]) < int(other.version[i])
                elif int(self.version[i]) == int(other.version[i]):
                    continue
                else:
                    return False
            # return self_version < other_version
        else:
            return NotImplemented

# TEST_5:
version = Version('12')
not_supported = ['12.0.0', 12.0, (12, 0), {12: 0}, True, False]

for obj in not_supported:
    print(obj == version)

# TEST_6:
version = Version('25')

print(version.__eq__(1))
print(version.__ne__(1.1))
print(version.__gt__(range(5)))
print(version.__lt__([1, 2, 3]))
print(version.__ge__({4, 5, 6}))
print(version.__le__({1: 'one'}))
