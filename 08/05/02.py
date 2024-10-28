import functools
def add_attr_to_class(*a, **kwa):
    def decorator(cls):
        for name, value in kwa.items():
            setattr(cls, name, value)
        return cls

    return decorator


# TEST_4:
@add_attr_to_class(shoot1='pif', shoot2='paf')
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()