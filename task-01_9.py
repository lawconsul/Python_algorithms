# -*- coding: utf-8 -*-
#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print("Введите 3 разных натуральных числа")

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите третье число: "))

if (x > y and x < z) or (x > z and x < y):
    res = x
else:
    if (y > x and y < z) or (y > z and y < x):
        res = y
    else:
        if (z > x and z < y) or (z > y and z < x):
            res = z

print(f': Cреднее между чисел: {res}')

