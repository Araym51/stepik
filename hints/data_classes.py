from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    balance: int


jack = Customer('jack', 500)
print(jack)
print(jack.__dict__)

"""
Попробуйте создать свой первый dataclass
Это будет простой класс Point, который должен хранить два целых атрибута x и y .
На основании класса Point создайте
    точку с координатами (5, 7) и сохраните ее в  переменную point1
    точку с координатами (-10, 12) и сохраните ее в  переменную point2
    Выведите сперва point1 потом на отдельной строке point2
"""

@dataclass
class Point:
    x: int
    y: int


point1 = Point(5,7)
point2 = Point(-10, 12)
print(point1)
print(point2)

"""
Создайте датакласс  Location
В нем должны быть описаны следующие атрибуты
name - обязательный, тип строка
longitude - необязательный, вещественный тип, значение по умолчанию 0
latitude - необязательный, вещественный тип, значение по умолчанию 11.5
Создайте ЭК Location со значениями name='Stonehenge', longitude=51, latitude=1.5  и сохраните его в переменную stonehenge
"""

@dataclass
class Location:
    name: str
    longitude: float = 0
    latitude: float = 11.5


stonehenge = Location(name='Stonehenge', longitude=51, latitude=1.5)
print(stonehenge)
