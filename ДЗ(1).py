"""
Дано число 28340928374 посчитать сумму цифр этого числа (генератор списков)
"""
numbers = 28340928374
sum_of_numbers = sum_of_numbers([int(i) for i in str(numbers)])
print(sum_of_numbers)