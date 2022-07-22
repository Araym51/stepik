"""
 Создайте класс Student, у которого есть:

конструктор __init__, принимающий 3 аргумента и создает приватные атрибуты __name, __age, __branch;
приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде
Имя: <name>
Возраст: <age>
Направление: <branch>
метод access_private_method, который вызывает приватный метод __display_details
Пример использования кода

#Output
Имя: Adam Smith
Возраст: 25
Направление: Information Technology
"""

class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\n'
              f'Возраст: {self.__age}\n'
              f'Направление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()


"""
В этом задании научимся просто вызывать защищенные и приватные методы у экземпляров класса.
Представьте, у вас есть вот такой класс


class PizzaMaker:
     def __make_pepperoni(self):
         ...

     def _make_barbecue(self):
         ...
Реализацию самих методов мы опустим. 
Ваша задача вызвать у экземпляра класса maker сперва метод _make_barbecue , затем метод __make_pepperoni . 
Именно в такой последовательности. Создавать класс вам не нужно, он уже создан и доступен, просто вам не виден
"""


class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass

print(PizzaMaker.__dict__.keys())
maker = PizzaMaker()
maker._make_barbecue()
maker._PizzaMaker__make_pepperoni()

