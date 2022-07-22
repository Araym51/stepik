"""
    Создайте базовый класс User, у которого есть:

    1. метод __init__, принимающий имя пользователя и его роль. Их необходимо сохранить в атрибуты экземпляра name и
role соответственно

Затем создайте класс Access , у которого есть:

    1. приватный атрибут класса __access_list , в котором хранится список ['admin', 'developer']
    2. риватный статик-метод __check_access , который принимает название роли и возвращает True, если роль
находится в списке __access_list , иначе - False
    3. публичный статик-метод get_access , который должен принимать экземпляр класса User и проверять
есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access  . Если у пользователя
достаточно прав, выведите на экран сообщение «User <name>: success», если прав недостаточно - «AccessDenied».
Если передается тип данных отличный от экземпляр класса Userнеобходимо вывести сообщение «AccessTypeError»
"""

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:

    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        if role.__dict__['role'] in Access.__access_list:
            return True
        else:
            return False

    @staticmethod
    def get_access(user):
        if isinstance(user, User):
            if Access.__check_access(user):
                print(f'User {user.__dict__["name"]}: success')
            else:
                print(f'AccessDenied')
        else:
            print('AccessTypeError')


user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError
