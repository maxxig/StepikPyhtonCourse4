import re
class CaseHelper:
    @staticmethod
    def is_snake(str):
        patter = r'^[a-z]{1,}([_][a-z]{1,}){0,}$'
        match = re.fullmatch(patter, str)
        return True if match != None else False
    @staticmethod
    def is_upper_camel(str):
        #patter = r'^([A-Z]{1}[a-z]{1,}){1,}$'
        patter = r'^([A-Z]{1}[a-z]{1,}){1}([A-Z]{1}[a-z]{1,}){0,}$'
        match = re.fullmatch(patter, str)
        return True if match != None else False
    @staticmethod
    def to_snake(str):
        patter = r'[A-Z]{1}[a-z]{1,}'
        match = re.findall(patter, str)
        return ('_'.join([s[0].lower()+s[1:] for s in match]))
    @staticmethod
    def to_upper_camel(str):
        patter = r'[a-z]{1,}'
        match = re.findall(patter, str)
        return (''.join([(s[0].upper()+s[1:]) for s in match]))

# INPUT DATA:

# TEST_1:
print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))

# TEST_2:
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))

# TEST_3:
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))

# TEST_4:
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))

# TEST_5:
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

for case in cases:
    print(CaseHelper.is_snake(case))

# TEST_6:
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']

for case in cases:
    print(CaseHelper.is_upper_camel(case))

# TEST_7:
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))

# TEST_8:
cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))

# TEST_9:
obj = CaseHelper()
print(type(obj.is_snake))
print(type(obj.is_upper_camel))
print(type(obj.to_snake))
print(type(obj.to_upper_camel))