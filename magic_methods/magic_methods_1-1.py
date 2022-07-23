"""
Создайте класс Person, у которого есть:

    1. конструктор __init__, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только
2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение,
печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender значением "male"
    2.переопределить метод __str__ следующим образом:
    - если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
    - если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
"""

class Person:
    def __init__(self, name, surname, gender = 'male'):
        self.name = name
        self.surname = surname
        self.gender = self.check(gender)

    def check(self, value):
        if isinstance(value, str):
            if value == 'male' or value == 'female':
                self.gender = value
                return self.gender
            else:
                self.gender = 'male'
                print(f"Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
                return self.gender
        else:
            self.gender = 'male'
            print(f"Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            return self.gender


    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
print(p1.__dict__)
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
print(p2.__dict__)
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"
print(p3.__dict__)