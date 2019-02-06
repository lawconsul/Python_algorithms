# -*- coding: utf-8 -*-
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import random

def create_arr(SIZE):
    min_item = 0
    max_item = 50
    array = [random.randint(min_item, max_item-1) for _ in range(SIZE)]
    return array

def get_mediana(arr):
    for i in range(0, len(arr)):  #цикл поиска медианы
        n, m = 0, 0     #счетчики бОльших и меньших значений
        for j in range(0, len(arr)):
            if arr[j] >= arr[i]:
                n += 1
            if arr[j] <= arr[i]:
                m += 1
        if n == m:
            return arr[i]

def print_result(arr, mediana):
    less, more = [], []
    for a in arr:
        if a <= mediana:
            less.append(a)
        if a >= mediana:
            more.append(a)
    print(f'Массив {arr} до сортировки')
    print(f'Элементы массива под медианой: ')
    print(', '.join(str(i) for i in less))
    print(f"Медиана: {mediana}")
    print(f'Элементы массива над медианой: ')
    print(', '.join(str(i) for i in more))



arr = create_arr(11)
print_result(arr, get_mediana(arr))

