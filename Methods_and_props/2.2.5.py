""" Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы
"Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"
Пример работы с классом Zebra"""


class Zebra:
    def __init__(self, a = 'Полоска белая', b = 'Полоска черная'):
        self.a = a
        self.b = b

    def which_stripe(self):
        print(self.a)
        self.a, self.b = self.b, self.a


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"


"""Создайте класс Person, у которого есть:
конструктор __init__, принимающий имя, фамилию и возраст. Их необходимо сохранить в атрибуты экземпляра first_name , last_name, age. 
метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"