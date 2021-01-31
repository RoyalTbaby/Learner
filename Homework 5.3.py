"""
Два натуральных числа называют дружественными,
если каждое из них равно сумме всех делителей другого,
кроме самого этого числа. Найти все пары дружественных чисел,
лежащих в диапазоне от 200 до 300.
"""

number = 0
for elem in range(200, 300):
    if elem != number:
        number1 = 0
        for i in range(1, elem // 2 + 1):
            if elem % i == 0:
                number1 += i
        number2 = 0
        for df in range(1, number1 // 2 + 1):
            if number1 % df == 0:
                number2 += df
        if number2 == elem != number1:
            print(elem, number1)
            f = number1