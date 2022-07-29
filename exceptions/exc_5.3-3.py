"""
Ниже представлен код. На предыдущем шаге мы выяснили, что могут возникнуть исключения типа ValueError и
ZeroDivisionError.
Ваша задача отловить их в одном блоке except и в случае возникновения любого из этих исключений вывести на
экран фразу «Введите корректные значения»
"""

try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a/b}")
except (ValueError, ZeroDivisionError):
    print('Введите корректные значения')

"""
Sample Input 1:
20
5
Sample Output 1:
Результат деления a на b: 4.0

Sample Input 2:
40
Somebody That I Used to Know
Sample Output 2:
Введите корректные значения

Sample Input 3:
5
0
Sample Output 3:
Введите корректные значения
"""
