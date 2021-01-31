"""
В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им все
четные по значению элементы.
"""

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
max_number = max(myList)
for i, val in enumerate(myList):
    if val % 2 == 0:
        myList[i] = max_number
print(myList)