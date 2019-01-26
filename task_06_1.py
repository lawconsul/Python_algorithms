# -*- coding: utf-8 -*-
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37)
# Darwin .local 18.2.0 Darwin Kernel Version 18.2.0: Mon Nov 12 20:24:46 PST 2018; root:xnu-4903.231.4~2/RELEASE_X86_64 x86_64

import sys
import random
import cProfile
from collections import deque
from functools import reduce


def show_size(x, sum_size, level=0):
    #print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    sum_size.append(sys.getsizeof(x))
    #print(f'sum_size = {sum_size}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, sum_size, level + 1)
                show_size(value, sum_size, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, sum_size, level + 1)


def analize_task(*args):
    sum_size = deque()
    for arg in args:
        show_size(arg, sum_size, 0)
    sum_sz = 0
    for value in sum_size:
        sum_sz += value

    print(f'Под все переменные из задачи было выделено {sum_sz} byte памяти ОЗУ')


def task_3_6_v1(SIZE, max_item):
    array = [random.randint(0, max_item) for _ in range(SIZE)]
    #print(f'Массив для анализа: {array}')

    dm = dict.fromkeys(['ind_of_min', 'ind_of_max', 'val_of_min', 'val_of_max'], 0)

    dm['val_of_min'] = array[0]
    dm['val_of_max'] = array[0]

    i = 0
    for i in range(0, len(array)):
        if array[i] < dm['val_of_min']:
            dm['ind_of_min'] = i
            dm['val_of_min'] = array[i]
        elif array[i] > dm['val_of_max']:
            dm['ind_of_max'] = i
            dm['val_of_max'] = array[i]

    start_, end_, sum_ = 0, 0, 0

    if dm['ind_of_max'] - dm['ind_of_min'] > 1:
        start_ = dm['ind_of_min']
        end_ = dm['ind_of_max']

    if dm['ind_of_min'] - dm['ind_of_max'] > 1:
        start_ = dm['ind_of_max']
        end_ = dm['ind_of_min']

    if start_ < end_:
        for i in range(start_ + 1, end_):
            sum_ += array[i]

    result = f'Сумма элементов массива: {sum_}'
    #print(result)


    analize_task(SIZE, max_item, array, dm, i, start_, end_, sum_)


def task_3_6_v2(SIZE, max_item):
    array = [random.randint(0, max_item) for _ in range(SIZE)]
    print(f'Массив для анализа: {array}')

    ind_of_min, ind_of_max, val_of_min, val_of_max = 0, 0, array[0], array[0]

    i = 0
    for i in range(0, len(array)):
        if array[i] < val_of_min:
            ind_of_min = i
            val_of_min = array[i]
        elif array[i] > val_of_max:
            ind_of_max = i
        val_of_max = array[i]

    start_, end_, sum_ = 0, 0, 0

    if ind_of_max - ind_of_min > 1:
        start_ = ind_of_min
        end_ = ind_of_max

    if ind_of_min - ind_of_max > 1:
        start_ = ind_of_max
        end_ = ind_of_min

    if start_ < end_:
        for i in range(start_ + 1, end_):
            sum_ += array[i]

    result = f'Сумма элементов массива: {sum_}'
    print(result)

    analize_task(SIZE, max_item, array, ind_of_min, ind_of_max, val_of_min, val_of_max, i, start_, end_, sum_)




def task_3_6_v3(SIZE, max_item):
    #SIZE = 10
    #max_item = 100
    array = deque(random.randint(0, max_item) for _ in range(SIZE))
    print(f'Массив для анализа: {array}')

    dm = dict.fromkeys(['ind_of_min', 'ind_of_max', 'val_of_min', 'val_of_max'], 0)

    dm['val_of_min'] = array[0]
    dm['val_of_max'] = array[0]

    i = 0
    for i in range(0, len(array)):
        if array[i] < dm['val_of_min']:
            dm['ind_of_min'] = i
            dm['val_of_min'] = array[i]
        elif array[i] > dm['val_of_max']:
            dm['ind_of_max'] = i
            dm['val_of_max'] = array[i]

    start_, end_, sum_ = 0, 0, 0

    if dm['ind_of_max'] - dm['ind_of_min'] > 1:
        start_ = dm['ind_of_min']
        end_ = dm['ind_of_max']

    if dm['ind_of_min'] - dm['ind_of_max'] > 1:
        start_ = dm['ind_of_max']
        end_ = dm['ind_of_min']

    if start_ < end_:
        for i in range(start_ + 1, end_):
            sum_ += array[i]

    result = f'Сумма элементов массива: {sum_}'
    print(result)


    analize_task(SIZE, max_item, array, dm, i, start_, end_, sum_)


# task_3_6_v1(10, 100)
# Первоначальная реализация на основе списка
# Под все переменные из задачи было выделено 1228 byte памяти ОЗУ

# task_3_6_v1(10000, 100000)
# Под все переменные из задачи было выделено 368380 byte памяти ОЗУ
# cProfile.run('task_3_6_v1(10000, 100000)')
# 1    0.002    0.002    0.039    0.039 task_06_1.py:40(task_3_6_v1)


# task_3_6_v2(10, 100)
# Реализация на основе списка, исключим словарь из 4х элементов
# Под все переменные из задачи было выделено 752 byte памяти ОЗУ
# task_3_6_v2(10000, 100000)
# Под все переменные из задачи было выделено 367904 byte памяти ОЗУ
# cProfile.run('task_3_6_v2(10000, 100000)')
# 1    0.005    0.005    0.053    0.053 task_06_1.py:79(task_3_6_v2)

#task_3_6_v3(10, 100)
# Реализация на основе очереди
# Под все переменные из задачи было выделено 1668 byte памяти ОЗУ
# task_3_6_v3(10000, 100000)
# Под все переменные из задачи было выделено 363748 byte памяти ОЗУ
# cProfile.run('task_3_6_v3(10000, 100000)')
# 1    0.007    0.007    0.049    0.049 task_06_1.py:116(task_3_6_v3)

# Выводы
# Оптимизация с размером особо заметна при небольших размерах массива
# Первоначальный вариант не самый экономный, зато он самый быстрый