# -*- coding: utf-8 -*-
#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input("Введите год (8-3000): "))
res = False
if year < 1582:
    if year % 4 == 0:
        res = True
else:
    if year % 400 == 0:
        res = True
    else:
        if year % 100 == 0:
            res = False
        else:
            if year % 4 == 0:
                res = True

if res == True:
    ans = "високосный"
else:
    ans = "невисокосный"

print(f': Год {year}: {ans}')

