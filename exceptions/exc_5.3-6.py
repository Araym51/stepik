"""
Мы уже имели честь познакомится с этим кодом.
Ваша задача отловить в блоке try-except именно возникающий тип исключения и вывести фразу
«Кто-то должен остановить это безумие»
"""

def func(phrase):
    func(phrase)
try:
    func('Это рекурсия, детка!')
except RecursionError:
    print('Кто-то должен остановить это безумие')