"""
    Создайте базовый класс  Person, у которого есть:

    1. конструктор __init__, который должен принимать на вход имя и номер паспорта и записывать их в атрибуты
name, passport
    2. метод display, который печатает на экран сообщение «<имя>: <паспорт>»;

    Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:

    1. метод  __init__, который принимает именно в таком порядке четыре значения: имя, паспорт, зарплату и отдел.
Их нужно сохранить в атрибуты  name, passport, salary,department. При этом создание атрибутов name, passport
необходимо делегировать базовому классу Person
"""

class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        return print(f'{self.name}: {self.passport}')


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department



a = Employee('Raul', 886012, 200000, "QA")
a.display()  # печатает "Raul: 886012"
