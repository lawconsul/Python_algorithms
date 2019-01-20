# -*- coding: utf-8 -*-

# 2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

hex_ = [('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('A', 10),
        ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15)]

def hex2int(hx):
    for key, value in hex_:
        if key == hx:
            return value

def int2hex(int):
    for key, value in hex_:
        if value == int:
            return key

A = str(input("Первое число: "))
B = str(input("Второе число: "))

a = deque(A.upper())
b = deque(B.upper())

a.reverse()
b.reverse()


#Суммирование
def sum_hex(a, b):
    max_len = max(a.__len__(), b.__len__())
    min_len = min(a.__len__(), b.__len__())

    if a.__len__() < max_len:
        for i in range(max_len - min_len):
            a.append('0')
    if b.__len__() < max_len:
        for i in range(max_len - min_len):
            b.append('0')

    c = deque()
    high_int = 0

    for i in range(max_len):
        sum_int = hex2int(a[i]) + hex2int(b[i]) + high_int
        high_int = sum_int // 16
        low_int = sum_int % 16

        high_hex = int2hex(high_int)
        low_hex = int2hex(low_int)
        c.append(low_hex)

        if i == max_len-1 and high_int > 0:
            c.append(high_hex)

    return c

#Вызов фунции суммирования
c = sum_hex(a, b)
c.reverse()
print(f'Сумма: {c}')


#Умножение
def mul_hex(a, b):
    mults = []

    for i in range(b.__len__()):
        d = deque()
        high_int = 0

        for z in range(i):
            d.appendleft("0")

        for j in range(a.__len__()):
            mul_int = hex2int(a[j]) * hex2int(b[i]) + high_int
            high_int = mul_int // 16
            low_int = mul_int % 16

            high_hex = int2hex(high_int)
            low_hex = int2hex(low_int)
            d.append(low_hex)

            if j == a.__len__() - 1 and high_int > 0:
                d.append(high_hex)

        mults.append(d)

    mul_res = deque("0")
    for t in mults:
        mul_res = sum_hex(mul_res, t)

    return mul_res

#Вызов фунции умножения
d = mul_hex(a, b)
d.reverse()
print(f'Умножение: {d}')
