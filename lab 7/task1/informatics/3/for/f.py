'''
Задача №338. Переверни число
Выведите число, состоящее из цифр данного числа x в обратном порядке. Ведущие нули выводить не нужно.
'''
a, res = input(), 0
n = int(a)
for i in range(len(a)):
    d = n % 10
    n //= 10
    res *= 10
    res += d
print(res)
