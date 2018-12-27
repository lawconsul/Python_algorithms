# -*- coding: utf-8 -*-
# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

dict29 = {a: 0 for a in range(2, 10)}

for i in range(2, 100):
    for a in dict29:
        if i % a == 0:
            dict29[a] += 1

print(f'{dict29}')
