import json
def jsonattr(filename):
    with open(filename) as f:
        data = json.load(f)
    def decorator(cls):
        for d in data:
            setattr(cls, d, data[d])
        return cls
    return decorator


# TEST_4:
with open('test.json', 'w') as file:
    file.write('{"shoot1": "pif", "shoot2": "paf"}')


@jsonattr('test.json')
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()