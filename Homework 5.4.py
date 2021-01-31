"""
Для заданного числа N составьте
программу вычисления суммы S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
"""


def calculate(n):
    sum = 0
    for elem in range(1, n + 1):
        sum = sum + (1 / elem)
    print("The sum is", round(sum, 2))


number = int(input('Enter a number: '))
calculate(number)