# -*- coding: utf-8 -*-
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

array[dm['ind_of_min']] = dm['val_of_max']
array[dm['ind_of_max']] = dm['val_of_min']

print(f'Измененный массив: {array}')
