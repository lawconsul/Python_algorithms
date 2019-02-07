# -*- coding: utf-8 -*-
# 1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import deque
import operator

class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def anal(letters):
    dictr = {}
    for letter in letters:
        if dictr.get(letter) is None:
            dictr[letter] = 1
        else:
            dictr[letter] = dictr.get(letter) + 1
    sorted_list = sorted(dictr.items(), key=operator.itemgetter(1))
    return sorted_list

def elem2node(elements):
    trees = deque()
    for element in elements:
        trees.append(MyNode(element[1], element[0]))
    return trees

def haff(trees):
    while trees.__len__() > 1:
        first = trees[0]
        second = trees[1]
        trees.popleft()
        trees.popleft()
        temp = deque()
        i = 0
        for tree in trees:
            if tree.value < first.value + second.value:
                temp.appendleft(tree)
                i += 1

        for j in range(i):
            trees.popleft()

        trees.appendleft(MyNode(first.value + second.value, first, second))
        trees.extendleft(temp)

    return trees[0]

def fix_left_leaf(bin_tree):
    if bin_tree.left is not None:
        if type(bin_tree.left) is str and bin_tree.right is None:
                bin_tree.value = bin_tree.left
                bin_tree.left = None

    if bin_tree.left is not None:
        fix_left_leaf(bin_tree.left)
    if bin_tree.right is not None:
        fix_left_leaf(bin_tree.right)


def gener_codes(bin_tree, dictr, path=''):
    if bin_tree.left is None and bin_tree.right is None:
        # print(f'{bin_tree.value} {path}')
        dictr.append((bin_tree.value, path))
    if bin_tree.left is not None:
        gener_codes(bin_tree.left, dictr, path=f'{path}0')
    if bin_tree.right is not None:
        gener_codes(bin_tree.right, dictr, path=f'{path}1')

def convert_dic_raw(dictr):
    dic = {}
    for row in dictr:
        dic[row[0]] = row[1]
    return dic

def crypto(phrase, dic):
    result = []
    for symbol in phrase:
        result.append(dic[symbol])
    return " ".join(result)

phrase = str(input("Введите строку из трех слов: "))
# phrase = str("beep boop beer!")
jungle = deque()
jungle.extend(anal(phrase))
jungle_nodes = elem2node(jungle)
haff_tree = haff(jungle_nodes)
fix_left_leaf(haff_tree)
dic_raw = []
gener_codes(haff_tree, dic_raw)
dic_haff = convert_dic_raw(dic_raw)
crypto_phrase = crypto(phrase, dic_haff)

print(f'Зашифрованная строка: {crypto_phrase}')
print(f'При шифровании использован словарь: {dic_haff}')

