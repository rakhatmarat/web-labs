'''
Задача №2936. Гипотенуза
Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.
'''

from math import *

a, b = int(input()), int(input())
print(sqrt(a ** 2 + b ** 2))
