# -*- coding: utf-8 -*-
# 2. Найти i-натуральное число

import math
import cProfile

#Тест простоты
def sieve(n):
    a = []
    s = []

    j = 0
    m = 0
    while m < n:
        if j < 2:
            a.append(0)
        else:
            a.append(j)
            simple = True
            for i in range(2,j):
                if simple is True:
                    if j % i == 0:
                        simple = False
            if simple is False:
                a[j] = 0
            else:
                m += 1
                s.append(j)
        j += 1

    #print(f'sieve({n}) = {s[len(s)-1]}')
    #print(s)
    #print(a)

#sieve(10)
cProfile.run('sieve(3000)')
#         1   16.924   16.924   16.928   16.928 task_04_2.py:8(sieve)



# 1000 loops, best of 3: 29.4 usec per loop - 10
# 1000 loops, best of 3: 5.57 msec per loop - 100
# 10 loops, best of 3: 1.38 sec per loop - 1000
# 1 loops, best of 3: 6.67 sec per loop - 2000
# 1 loops, best of 3: 16.6 sec per loop - 3000



#Тест простоты
# Предлагаю исключить из проверки числа, кратные 5 и 10
# а также ввести проверку (i * i - 1 > j)
def no_sieve(n):
    a = []
    s = []

    j = 0
    m = 0
    while m < n:
        if j < 2:
            a.append(0)
        else:
            a.append(j)
            simple = True

            if j > 5:
                # if j % 5 != 0 and j % 10 != 0 or j == 5:
                if str(j)[-1] == "5" or str(j)[-1] == "0":
                    simple = False

            if simple is True:
                z = int(math.sqrt(j+1))
                for i in range(2,j):
                    if i * i - 1 > j:
                        continue
                    else:
                        if j % i == 0:
                            simple = False
                if simple is False:
                    a[j] = 0
                else:
                    m += 1
                    s.append(j)
        j += 1

    #print(f'no_sieve({n}) = {s[len(s)-1]}')
    #print(s)
    #print(a)

# no_sieve(100)
# cProfile.run('no_sieve(3000)')
# 1 loops, best of 3: 33 sec per loop

# 1000 loops, best of 3: 59.9 usec per loop - 10
# 100 loops, best of 3: 12.4 msec per loop - 100
# 10 loops, best of 3: 2.71 sec per loop - 1000
# 1 loops, best of 3: 33 sec per loop - 3000

# Итоги: вторым способом может быть и экономится память, но времени уходит гораздо больше

