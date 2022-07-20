"""
Далее создайте класс  Trash у которого есть:

    1. атрибут класса  content изначально равный пустому списку
    2. статик-метод  add, который принимает файл и сохраняет его в корзину: для этого нужно добавить его в атрибут
content и проставить файлу атрибут in_trash значение True. Если в метод add передается не экземпляр класса File,
необходимо вывести сообщение «В корзину добавлять можно только файл»
    3. статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов,
хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла remove. Атрибут content
после очистки должен стать пустым списком. Сама процедура очистки должна начинаться фразой «Очищаем корзину» и
заканчиваться фразой «Корзина пуста»
    4. статик-метод  restore, который запускает процесс восстановления файлов из корзины. Необходимо для всех файлов,
хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла restore_from_trash.
Атрибут content  после очистки должен стать пустым списком. Сама процедура восстановления должна начинаться
фразой «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»
"""

class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        self.in_trash = False
        print(f'Файл {self.name} восстановлен из корзины')

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def remove(self):
        self.is_deleted = True
        print(f'Файл {self.name} был удален')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []

    @staticmethod
    def add(file):
        pass

    @staticmethod
    def clear():
        pass

    @staticmethod
    def restore():
        pass


f1 = File('puppies.jpg')
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)

Trash.add(f2)
Trash.add(passwords)
Trash.clear() # после этой команды вывод должен быть таким
'''
Очищаем корзину
Файл puppies.jpg был удален
Файл cat.jpg был удален
Файл pass.txt был удален
Корзина пуста
'''

f1.read() # ErrorReadFileTrashed(puppies.jpg)
