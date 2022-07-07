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


class Stack:

    def __init__(self, obj_list = []):
        self.obj_list = obj_list

    def push(self, data):
        self.obj_list.append(data)

    def peek(self):
        if self.is_empty():
            print(f'Empty Stack'),
            return None
        else:
            return self.obj_list[-1]

    def is_empty(self):
        if len(self.obj_list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.obj_list)

    def pop(self):
        if self.is_empty():
            self.peek()
        else:
            return self.obj_list.pop()


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2
