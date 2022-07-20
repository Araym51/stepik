"""
Создайте класс  File, у которого есть:

    1. метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name.
Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False
    2. метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» и проставляет атрибут
in_trash в значение False
    3. метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True
    4. метод read, который
        - печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
        - печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
        - печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине
    5. метод write, который принимает значение content для записи и
        - печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
        - печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
        - печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине
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
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')


f1 = File('puppies.jpg')
print(f1.__dict__)  # {'name': 'puppies.jpg', 'in_trash': False, 'is_deleted': False}
f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
f1.read()  # ErrorReadFileDeleted(puppies.jpg)

f2 = File('cat.jpg')
f2.write('hello')  # Записали значение hello в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)
