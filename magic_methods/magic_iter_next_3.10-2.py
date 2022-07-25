"""
Создайте класс InfinityIterator, который реализует бесконечный итератор, который будет при каждой новой итерации или
вызовы функции next будет возвращать число, увеличенное на 10 от предыдущего значения. Начинать нужно с нуля.
"""

class InfinityIterator:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        num = self.number
        self.number += 10
        return num


a = iter(InfinityIterator())
next(a)
next(a)
next(a)
next(a)
