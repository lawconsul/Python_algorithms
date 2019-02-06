# -*- coding: utf-8 -*-
# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

def create_arr(SIZE):
    #SIZE = 10
    min_item = -100
    max_item = 100
    array = [random.randint(min_item, max_item-1) for _ in range(SIZE)]
    return array

def sort_bubble_desc(arr):
    print(f'Массив {arr} до сортировки')
    n = 1
    while n < len(arr):
        ideal = True
        for i in range(len(arr)-1):

            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                ideal = False
        if ideal is True:
            print(f'Массив {arr} отсортирован по убыванию методом пузырька на {n}-шаге')
            return
        n += 1
    print(f'Массив {arr} отсортирован по убыванию методом пузырька')


arr = create_arr(10)
sort_bubble_desc(arr)