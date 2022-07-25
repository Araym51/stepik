"""
    Создайте класс PowerTwo, который возвращает следующую степень двойки, начиная с нулевой степени (20=1).
Внутри класса реализуйте:
    1. метод __init__. Он должен принимать одно положительное число - степень двойки, до которой нужно
итеририроваться включительно (см пример ниже)
    2. методы __iter__ и __next__ для итерирования по степеням двойки

"""

class PowerTwo:
    def __init__(self, iter):
        self.iter = iter
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.iter:
            num = 2 ** self.index
            self.index += 1
            return num
        else:
            raise StopIteration


numbers = PowerTwo(2)

iterator = iter(numbers)

print(next(iterator)) # печатает 1
print(next(iterator)) # печатает 2
print(next(iterator)) # печатает 4
print(next(iterator)) # исключение StopIteration

for i in PowerTwo(4): # итерируемся до 4й степени двойки
    print(i)
"""
Цикл выше печатает следующие числа
1
2
4
8
16
"""
