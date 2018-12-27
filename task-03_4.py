# -*- coding: utf-8 -*-
# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
max_item = 10
array = [random.randint(1, max_item) for _ in range(SIZE)]
print(f'Массив для анализа: {array}')

d = {}
for i in range(0, len(array)):
    if d.get(array[i], 0) == 0:
        d[array[i]] = d.get(array[i], 1)
    else:
        d[array[i]] = d.get(array[i], 1) + 1

max_rep = 0
arr_rep = []

for k in d:
    if d[k] > max_rep:
        max_rep = d[k]
for k in d:
    if d[k] == max_rep:
        arr_rep.append(k)

print(f'Самые встречающиеся ({max_rep}-раза) числа в массиве: {arr_rep}')
