"""
Введите число. Если это число делиться на 1000
без остатка, то выведите на
экран "millennium"
"""

number = int(input("Enter a number: "))
if not number % 1000:
    print("millennium")