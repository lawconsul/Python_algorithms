# -*- coding: utf-8 -*-
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC
# Нагло передрал текст из примера сортировки на языке С )

import random

def create_arr(SIZE):
    min_item = 0
    max_item = 50
    array = [random.randint(min_item, max_item-1) for _ in range(SIZE)]
    return array

def create_null_arr(SIZE):
    array = [None for _ in range(SIZE)]
    return array

def merge_sort(up, down, left, right):
    if left == right:
        down[left] = up[left]
        return down

    middle = (left + right) // 2

    # разделяй и властвуй
    l_buff = merge_sort(up, down, left, middle)
    #print(up, down, left, middle)
    r_buff = merge_sort(up, down, middle + 1, right)
    #print(up, down, middle + 1, right)

    # слияние двух отсортированных половин
    if l_buff == up:
        target = down
    else:
        target = up

    l_cur = left
    r_cur = middle + 1

    for i in range(left, right+1):
        if l_cur <= middle and r_cur <= right:
            if l_buff[l_cur] < r_buff[r_cur]:
                target[i] = l_buff[l_cur]
                l_cur += 1
            else:
                target[i] = r_buff[r_cur]
                r_cur += 1
        elif l_cur <= middle:
            target[i] = l_buff[l_cur]
            l_cur += 1
        else:
            target[i] = r_buff[r_cur]
            r_cur += 1
    return target

size = 100
arr = create_arr(size)
print(f'Массив {arr} до сортировки')
tmp = create_null_arr(size)
depth = []
merge_sort(arr, tmp, 0, len(arr)-1)
print(f'Массив {tmp} отсортирован по возрастанию методом слияния c глубиной {2*size-1}')

