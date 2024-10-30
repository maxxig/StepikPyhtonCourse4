from dataclasses import dataclass
@dataclass
class City:
    name: str
    population: str
    founded : int

# TEST_5:
city1 = City('Ростов', 1142162, 1749)
city2 = City('Владивосток', 605049, 1860)

print(city1)
print(city1.name)
print(city1.population)
print(city1.founded)

print(city2)
print(city2.name)
print(city2.population)
print(city2.founded)

print(city2 == city2)
print(city1 != city2)