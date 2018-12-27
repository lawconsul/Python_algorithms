# -*- coding: utf-8 -*-
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZErow = 4
SIZEcol = 6
max_item = 10
array = []

print(f'Массив для анализа:')
for i in range(SIZErow):
    arr = []
    for j in range(SIZEcol):
        arr.append(random.randint(0, max_item))
    array.append(arr)
    print(arr)

print(f'Минимальные значения столбцов:')

arr_mini = []
for j in range(SIZEcol):
    mini = array[0][j]
    for i in range(1, SIZErow):
        if array[i][j] < mini:
            mini = array[i][j]
    arr_mini.append(mini)
    print(mini, end = ', ')

maxi = arr_mini[0]
for j in range(1, len(arr_mini)):
    if arr_mini[j] > maxi:
        maxi = arr_mini[j]

print(f'\nМаксимальное из минимальных значений столбцов: {maxi}')