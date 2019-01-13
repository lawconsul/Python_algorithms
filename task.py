# -*- coding: utf-8 -*-
# 1. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# В ДЗ-3 к уроку №3, я не учел случай, когда возможно более 1 мксимального или минмального значения
# В ДЗ-1 у уроку №4 я возьму во внимание этот случай.


import random
import cProfile
import numpy as np



def gener_array(SIZE):
    max_item = 100
    arr = [random.randint(0, max_item) for _ in range(SIZE)]
    return arr

def chngMM(arr):
    ind_of_min = []
    ind_of_max = []
    val_of_min = arr[0]
    val_of_max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < val_of_min:
            ind_of_min = []
            ind_of_min.append(i)
            val_of_min = arr[i]

        elif arr[i] == val_of_min:
            ind_of_min.append(i)

        if arr[i] > val_of_max:
            ind_of_max = []
            ind_of_max.append(i)
            val_of_max = arr[i]

        elif arr[i] == val_of_max:
            ind_of_min.append(i)

    for i in ind_of_min:
        arr[i] = val_of_max

    for i in ind_of_max:
        arr[i] = val_of_min


# 1. Версия без изменений
def main(SIZE):
    arr = gener_array(SIZE)
    chngMM(arr)

#radik$ python -m timeit -n 1000 -s "import task" "task.main(100)"
#1000 loops, best of 3: 141 usec per loop - 100
#100 loops, best of 3: 1.4 msec per loop - 1 000
#100 loops, best of 3: 12.7 msec per loop - 10 000
#10 loops, best of 3: 166 msec per loop - 100 000
# 10 loops, best of 3: 1.66 sec per loop - 1 000 000
# 1 loops, best of 3: 17.5 sec per loop - 10 000 000
# 1 loops, best of 3: 166 sec per loop - 100 000 000


#cProfile.run('main(10000000)')

#   Время увеличивается линейно в зависимости от заданного кол-ва элементов массива
#   Предлагаю заменить  ф-цию randint ее аналогом из библиотеки numpy
#        1    0.000    0.000    0.000    0.000 task.py:46(main) - 100
#        1    0.000    0.000    0.003    0.003 task.py:46(main) - 1000
#        1    0.000    0.000    0.027    0.027 task.py:46(main) - 10 000
#        1    0.000    0.000    0.277    0.277 task.py:46(main) - 100 000
#        1    0.000    0.000    2.596    2.596 task.py:46(main) - 1 000 000
#        1    0.003    0.003   25.336   25.336 task.py:46(main) - 10 000 000

 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.020    0.020   25.355   25.355 <string>:1(<module>)
 # 10000000    7.733    0.000   16.448    0.000 random.py:173(randrange)
 # 10000000    3.375    0.000   19.823    0.000 random.py:217(randint)
 # 10000000    5.997    0.000    8.715    0.000 random.py:223(_randbelow)
 #        1    0.000    0.000   22.881   22.881 task.py:10(gener_array)
 #        1    3.058    3.058   22.881   22.881 task.py:12(<listcomp>)
 #        1    2.432    2.432    2.452    2.452 task.py:15(chngMM)
 #        1    0.003    0.003   25.336   25.336 task.py:46(main)
 #        1    0.000    0.000   25.355   25.355 {built-in method builtins.exec}





# 2. Версия генератор с библиотекой numpy

def gener_array_numpy(SIZE):
    max_item = 100
    arr = np.random.random_integers(max_item, size=SIZE)
    #print(f'Массив для анализа: {arr}')
    return arr

def main_np(SIZE):
    #arr = []
    arr = gener_array_numpy(SIZE)
    chngMM(arr)

#radik$ python -m timeit -n 1000 -s "import task" "task.main_np(100)"

# 1000 loops, best of 3: 70.8 usec per loop - 100
# 1000 loops, best of 3: 652 usec per loop - 1000
# 100 loops, best of 3: 6.43 msec per loop - 10 000
# 100 loops, best of 3: 63.9 msec per loop - 100 000
# 10 loops, best of 3: 643 msec per loop - 1 000 000
# 1 loops, best of 3: 7.32 sec per loop - 10 000 000



#cProfile.run('main_np(10000000)')

# Ф-ция randint из библиотеки numpy быстрее аналога в 100+ раз
# Но функция поиска и замены при работе с массивом, полученным от randint из библиотеки numpy,
# медленнее в 2 раза, чем стандартный аналог
# Предлагаю в 3-м варианте заменить также ф-цию поиска ее аналогами из библиотеки numpy

#        1    0.000    0.000    0.001    0.001 task.py:91(main_np) - 100
#        1    0.000    0.000    0.001    0.001 task.py:91(main_np) - 1 000
#        1    0.000    0.000    0.007    0.007 task.py:91(main_np) - 10 000
#        1    0.000    0.000    0.068    0.068 task.py:91(main_np) - 100 000
#        1    0.000    0.000    0.708    0.708 task.py:91(main_np) - 1 000 000
#        1    0.004    0.004    6.702    6.702 task.py:91(main_np) - 10 000 000
#
#        1    6.507    6.507    6.531    6.531 task.py:15(chngMM)
#        1    0.000    0.000    0.167    0.167 task.py:85(gener_array_numpy)
#        1    0.004    0.004    6.702    6.702 task.py:91(main_np)


# 3. Версия генератор с библиотекой numpy + поиск с библиотекой numpy

def chngMM_numpy(arr):
    val_min = arr.min()
    val_max = arr.max()

    ind_min = np.where(arr == val_min)
    ind_of_min = list(ind_min)

    ind_max = np.where(arr == val_max)
    # ind_of_max = [idx[0] for idx in ind_max]
    ind_of_max = list(ind_max)

    for i in ind_of_min:
        arr[i] = val_max

    for i in ind_of_max:
        arr[i] = val_min

    # print(f'ind_of_min: {ind_of_min}')
    # print(f'ind_of_max: {ind_of_max}')
    # print(f'val_of_min: {val_min}')
    # print(f'val_of_max: {val_max}')


def main_np_3(SIZE):
    #arr = []
    arr = gener_array_numpy(SIZE)
    #tp = type(arr)
    # print(f'Массив для анализа: {arr}')
    chngMM_numpy(arr)
    # print(f'Измененный массив: {arr}')

# radik$ python -m timeit -n 1000 -s "import task" "task.main_np_3(100)"
# 1000 loops, best of 3: 16.7 usec per loop - 100
# 1000 loops, best of 3: 32.6 usec per loop - 1 000
# 1000 loops, best of 3: 164 usec per loop - 10 000
# 1000 loops, best of 3: 1.49 msec per loop - 100 000
# 100 loops, best of 3: 16.3 msec per loop - 1 000 000
# 10 loops, best of 3: 164 msec per loop - 10 000 000
# 1 loops, best of 3: 2.08 sec per loop - 100 000 000

# cProfile.run('main_np_3(1000000000)')
#         1    0.000    0.000    0.000    0.000 task.py:150(main_np_3) - 100
#         1    0.000    0.000    0.000    0.000 task.py:150(main_np_3) - 1000
#         1    0.000    0.000    0.000    0.000 task.py:150(main_np_3) - 10 000
#         1    0.000    0.000    0.002    0.002 task.py:150(main_np_3) - 100 000
#         1    0.000    0.000    0.022    0.022 task.py:150(main_np_3) - 1 000 000
#         1    0.000    0.000    0.241    0.241 task.py:150(main_np_3) - 10 000 000

#         1    0.024    0.024    0.060    0.060 task.py:127(chngMM_numpy)
#         1    0.000    0.000    0.241    0.241 task.py:150(main_np_3)
#         1    0.000    0.000    0.181    0.181 task.py:85(gener_array_numpy)

#         1    0.002    0.002    4.008    4.008 task.py:150(main_np_3) - 100 000 000

#         1    0.000    0.000    0.126    0.126 _methods.py:25(_amax)
#         1    0.000    0.000    1.212    1.212 _methods.py:28(_amin)
#         1    0.551    0.551    1.991    1.991 task.py:127(chngMM_numpy)
#         1    0.002    0.002    4.008    4.008 task.py:150(main_np_3)
#         1    0.000    0.000    2.016    2.016 task.py:85(gener_array_numpy)


# Ф-ция поиска и замены, использующая ф-ии min() и max() из библиотеки numpy, оказалась быстрее аналога в 40+ раз
# Но функция  при работе с массивом, полученным от randint из библиотеки numpy, медленне в 2 раза чем стандартный аналог

#Кол-во         100             100 000             100 000 000
#1-ый           141 usec        166 msec            166 sec
#2-ый           70.8 usec       63.9 msec           72.9 sec
#3-ый           16.7 usec       1.49 msec           2.08 sec

# Вывод: Использование библиотеки numpy позволяет сократить общее время выполнения
# на небольших по размеру массивах (<100 элементов) в 9 раз
# на больших по размеру массивах (100 000 элементов) в 110 раз  - numpy более эффективен при использовании на больших
# на огромных по размеру массивах (>100 000 000 элементов) в 80 раз - эффективность numpy начинает по-немногу падать
