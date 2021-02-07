"""
Дано число 28340928374 посчитать сумму цифр этого числа (генератор списков)
"""

from functools import reduce

numbers = 28340928374
new_list = [int(i) for i in str(numbers)]


def do_sum(x1, x2):
    return x1 + x2


print(reduce(do_sum, new_list))
