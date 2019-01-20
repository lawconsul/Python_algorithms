# -*- coding: utf-8 -*-

# 1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import deque
from collections import namedtuple
from functools import reduce

Company = namedtuple('Company', 'name ap q1 q2 q3 q4')

n = int(input("Количество компаний: "))
companies = deque(maxlen=n)
average_profit = 0
total_average_profit = 0

for i in range(n):
    cname = input(str(i + 1) + "-я компания: ")

    profit = {'q1': 0, 'q2': 0, 'q3': 0, 'q4': 0}
    profit['q1'] = float(input("Прибыль за 1-й картал: "))
    profit['q2'] = float(input("Прибыль за 2-й картал: "))
    profit['q3'] = float(input("Прибыль за 3-й картал: "))
    profit['q4'] = float(input("Прибыль за 4-й картал: "))
    average_profit = (reduce(lambda a, b: a + b, profit.values())) / 4
    total_average_profit += average_profit

    company_i = Company(cname, average_profit, **profit)
    companies.append(company_i)

total_average_profit = total_average_profit / n

g_tap = deque()
l_tap = deque()

for company_i in companies:
    if company_i.ap > total_average_profit:
        g_tap.append(company_i.name)
    if company_i.ap < total_average_profit:
        l_tap.append(company_i.name)

if len(g_tap) > 0:
    print(f"Прибыль выше средней: ")
    for name in g_tap:
        print(f"{name}")
if len(l_tap) > 0:
    print(f"Прибыль ниже средней: ")
    for name in l_tap:
        print(f"{name}")
