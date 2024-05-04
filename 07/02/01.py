class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'
class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99$'
class GoldPlan(SilverPlan):
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'

# TEST_4:
print(issubclass(SilverPlan, BasicPlan))
print(issubclass(GoldPlan, BasicPlan))