"""
Дано число. Найти сумму и произведение его цифр.
"""

n = int(input("Enter a number: "))
summ = 0
multiplier = 1 #при умножении на ноль будет ноль

while n > 0:
    division = n % 10  #избавляемся от последней цифры числа, поделив его на 10
    summ = summ + division
    multiplier = multiplier * division
    n = n // 10

print(summ)
print(multiplier)