# -*- coding: utf-8 -*-
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
max_item = 100
array = [random.randint(0, max_item) for _ in range(SIZE)]
print(f'Массив для анализа: {array}')


dm = dict.fromkeys(['ind_of_min', 'ind_of_max', 'val_of_min', 'val_of_max'], 0)

dm['val_of_min'] = array[0]
dm['val_of_max'] = array[0]

for i in range(0, len(array)):
    if array[i] < dm['val_of_min']:
        dm['ind_of_min'] = i
        dm['val_of_min'] = array[i]
    elif array[i] > dm['val_of_max']:
        dm['ind_of_max'] = i
        dm['val_of_max'] = array[i]

start_ = 0
end_ = 0
sum_ = 0;

if dm['ind_of_max'] - dm['ind_of_min'] > 1:
    start_ = dm['ind_of_min']
    end_ = dm['ind_of_max']

if dm['ind_of_min'] - dm['ind_of_max'] > 1:
    start_ = dm['ind_of_max']
    end_ = dm['ind_of_min']

if start_ < end_:
    for i in range(start_ + 1, end_):
        sum_ += array[i]


print(f'Сумма элементов массива: {sum_}')