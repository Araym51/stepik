"""
Создайте класс Rectangle, у которого есть:

конструктор __init__, принимающий 2 аргумента: длину и ширину.
свойство area, которое возвращает площадь прямоугольника;
"""

class Rectangle:
    def __init__(self, lenght, height):
        self.__lenght = lenght
        self.__height = height
        self.__area = None

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        self.__lenght = value
        self.__area = None

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__height * self.__lenght
        return self.__area


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area) # 15
print(r2.area) # 6


"""
  Создайте класс Date, у которого есть:
1. конструктор __init__, принимающий 3 аргумента: день, месяц и год. 
2. свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
3. свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";

Обратите внимание, что дни и месяцы занимают 2 символа в выводе, а отображение года- 4 символа
(заполняются нулями спереди до нужной длины). 
"""

class Date:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value

    @property
    def date(self):
        return f'{self.__day:02}/{self.__month:02}/{self.__year:04}'

    @property
    def usa_date(self):
        return f'{self.__month:02}-{self.__day:02}-{self.__year:04}'


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999
