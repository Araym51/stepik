"""У нас уже имеется с предыдущего урока класс Registration. Давайте добавим в него следующее:

    1. в метод  __init__ добавляется еще один аргумент: пароль. Как в примере с логином, вы должны будете сохранить
переданный пароль через password через сеттер  password (см пункт 3 в этом задании). Примерный код метода __init__
def __init__(self, логин, пароль):
    self.login = логин # передаем в сеттер login значение логин
    self.password = пароль # передаем в сеттер password значение пароль
Должны сработать свойства сеттер login из предыдущего задания  и сеттер password из пункта 3 для проверки
валидности переданных значений

    2. Свойство геттер password, которое возвращает значение self.__password;
    3. Свойство сеттер password, принимает значение нового пароля. Его необходимо перед сохранением проверить на
следующее:
    - новое значение пароля должно быть строкой(не список, словарь и т.д. ) в противном случае вызываем исключение
TypeError("Пароль должен быть строкой")
    - Длина нового пароля должна быть от 5 до 11 символов, в противном случае вызывать исключение
ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
    - Новый пароль должен содержать хотя бы одну цифру. Для этого создаем staticmethod is_include_digit , который
проходит по всем элементам строки и проверяет наличие цифр. В случае отсутствия цифрового символа вызываем исключение:
ValueError('Пароль должен содержать хотя бы одну цифру')
    - Строка password должна содержать элементы верхнего и нижнего регистра.
Создаем staticmethod is_include_all_register, который с помощью цикла проверяет элемента строчки на регистр.
В случае ошибки вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
    - Строка password помимо цифр должна содержать только латинские символы. Для этого создайте
staticmethod is_include_only_latin , который проверяет каждый элемент нового значения на принадлежность к
латинскому алфавиту(проверка должна быть как в верхнем, так и нижнем регистре). В случае, если встретится нелатинский
символ, вызвать ошибку ValueError('Пароль должен содержать только латинский алфавит').
Подсказка: из модуля string можно импортировать переменную ascii_letters, она хранит в себе все латинские
символы в верхнем и нижнем регистре
    - Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt.
Сохраните данный файл к себе в папку с вашей программой и не меняйте название. С помощью staticmethod
создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле. Если значение совпадет
со значением из файла, то в сеттер вызываем исключение: ValueError('Ваш пароль содержится в списке самых легких')
"""

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    def set_email(self, email):
        if isinstance(email, str) and email.count('@') == 1:
            if '.' in email[email.find('@'):]:
                return True
            else:
                raise ValueError("Логин должен содержать символ '.'")
        else:
            raise ValueError("Логин должен содержать один символ '@'")

    @login.setter
    def login(self, value):
        if self.set_email(value):
            self.__login = value

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(value):
        for item in value:
            if item.isdigit():
                return True
        return False

    @staticmethod
    def is_include_all_register(value):
        upper = 0
        lower = 0
        for _ in value:
            if _.isdigit():
                pass
            else:
                if _.isupper():
                    upper += 1
                if _.islower():
                    lower += 1
        if upper > 0 and lower > 0:
            return True
        else:
            return False

    @staticmethod
    def is_include_only_latin(value):
        for _ in value:
            if not _.isascii():
                return False
        return True

    @staticmethod
    def check_password_dictionary(value):
        with open('easy_passwords.txt', 'r') as passwords:
            for _ in passwords:
                if _.strip() == value:
                    return False
        return True

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(value) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value



r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 'KissasSAd1f'  # raise TypeError("Пароль должен быть строкой")