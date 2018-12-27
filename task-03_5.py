# -*- coding: utf-8 -*-
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 100
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print(f'Массив для анализа: {array}')

ind_of_max = 0
val_of_max = 0
for i in range(0, len(array)):
    if array[i] < 0:
        if val_of_max == 0:
            ind_of_max = i
            val_of_max = array[i]
        else:
            if array[i] > val_of_max:
                ind_of_max = i
                val_of_max = array[i]


print(f'Максимальное отрицательное число в массиве: {val_of_max}, его индекс: {ind_of_max}')
