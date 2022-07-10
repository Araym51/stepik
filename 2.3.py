"""
Создайте класс Dog, у которого есть:
метод __init__, принимающий имя и возраст собаки и сохраняющий их в аргументы name и age
метод description, который возвращает строку в виде «{name} is {age} years old»
метод speak принимающий один аргумент, который возвращает строку вида «{name} says {sound}»
"""

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self, voice):
#         self.voice = voice
#         return f'{self.name} says {self.voice}'
#
#
# jack = Dog("Jack", 4)
#
# print(jack.description()) # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'



"""
Ваша задача реализовать класс Stack, у которого есть:

метод __init__создаёт новый пустой стек. Параметры данный метод не принимает. Создает атрибут экземпляра values, где 
будут в дальнейшем хранятся элементы стека в виде списка (list), изначально при инициализации задайте значение атрибуту 
values равное пустому списку;

метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает.
метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. Стек изменяется. 
Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "Empty Stack";
метод peek() возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется. 
Если элементов в стеке нет, распечатайте сообщение "Empty Stack", верните None после этого;
метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.
метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число.
"""

# class Stack:
#
#     def __init__(self, obj_list = []):
#         self.obj_list = obj_list
#
#     def push(self, data):
#         self.obj_list.append(data)
#
#     def peek(self):
#         if self.is_empty():
#             print(f'Empty Stack'),
#             return None
#         else:
#             return self.obj_list[-1]
#
#     def is_empty(self):
#         if len(self.obj_list) == 0:
#             return True
#         else:
#             return False
#
#     def size(self):
#         return len(self.obj_list)
#
#     def pop(self):
#         if self.is_empty():
#             self.peek()
#         else:
#             return self.obj_list.pop()
#
#
# s = Stack()
# s.peek()  # распечатает 'Empty Stack'
# print(s.is_empty())  # распечатает True
# s.push('cat')  # кладем элемент 'cat' на вершину стека
# s.push('dog')  # кладем элемент 'dog' на вершину стека
# print(s.peek())  # распечатает 'dog'
# s.push(True)  # кладем элемент True на вершину стека
# print(s.size())  # распечатает 3
# print(s.is_empty())  # распечатает False
# s.push(777)  # кладем элемент 777 на вершину стека
# print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
# print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
# print(s.size())  # распечатает 2

"""
Создайте класс Worker, у которого есть:

метод __init__, принимающий 4 аргумента: имя, зарплата, пол и паспорт. Необходимо сохранить их в следующих атрибутах: 
name, salary, gender и passport.
свойство get_info, которое распечатает информацию о сотруднике в следующем виде: «Worker {name}; passport-{passport}»
Пример использования класса Worker

bob = Worker('Bob Moore', 330000, 'M', '1635777202')
bob.get_info() # печатает "Worker Bob Moore; passport-1635777202"
Ниже имеется список кортежей persons, содержащий информацию о десяти работниках. На основании этих данных необходимо 
создать 10 экземпляров класса Worker и добавить их в список  worker_objects. Работников в списке следует разместить 
в том же порядке, в каком они встречаются в списке persons.

В этом же порядке для каждого объекта в списке worker_objects вызовите метод get_info
"""

# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
#
# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         return print(f'Worker {self.name}; passport-{self.passport}')
#
#
# worker_objects = []
# for worker in persons:
#     person = Worker(worker[0], worker[1], worker[2], worker[3])
#     worker_objects.append(person)
#
# for info in worker_objects:
#     info.get_info()


"""
Ваша задача  создать класс CustomLabel, у которого есть:
- метод __init__, принимающий один обязательный аргумент текст виджета, его необходимо сохранить в атрибут text. 
И также в метод  может поступать произвольное количество именованных аргументов. Их необходимо сохранять в 
атрибуты экземпляра под тем же названием
- метод config, который принимает произвольное количество именованных атрибутов. Он должен создать атрибут 
с указанным именем или, если этот атрибут уже присутствовал в экземпляре, изменить его на новое значение
"""


# class CustomLabel:
#     def __init__(self, text, **kwargs):
#         self.text = text
#         for key, value in kwargs.items():
#             self.__dict__[key] = value
#
#     def config(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#
# label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
# print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
# label.config(color='red', bd=100)
# print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}

"""  
Создайте базовый класс Person, у которого есть:
1 метод __init__, принимающий имя и возраст человека. Их необходимо сохранить в атрибуты экземпляра name и age 
соответственно
2 метод display_person_info , который печатает информацию в следующем виде:
    Person: {name}, {age}

Затем создайте класс Company , у которого есть:
1 метод __init__, принимающий название компании и город ее основания. Их необходимо сохранить в атрибуты 
экземпляра company_name  и location соответственно
2 метод display_company_info , который печатает информацию в следующем виде:
    Company: {company_name}, {location}

И в конце создайте класс Employee , который:
1 имеет метод __init__, принимающий имя человека, его возраст, название компании и город основания. 
Необходимо создать атрибут personal_data и сохранить в него экземпляр класса Person. 
И также создать атрибут work  и сохранить в него экземпляр класса Company 
2 После этого через атрибуты personal_data и work  вы можете обращаться к методам соответствующих
классов Person и Company 
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        return print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        return print(f'Company: {self.company_name}, {self.location}')


class Employee:
    def __init__(self, name, age, company_name, location):
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)



emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()