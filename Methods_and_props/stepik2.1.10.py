"""
Создайте класс Point. У этого класса должны быть

метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса соответственно
в атрибуты x и y
метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между двумя точками
по теореме Пифагора. В случае, если в данный метод передается не экземпляр класса Point
необходимо вывести сообщение "Передана не точка"
Пример работы с классом Point
"""


class Point:
    def set_coordinates(self, x, y):
        setattr(self, 'x', x)
        setattr(self, 'y', y)

    def get_distance(self, obj):
        if isinstance(obj, Point):
            self.result = ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) ** 0.5
            return self.result
        else:
            print("Передана не точка")


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"