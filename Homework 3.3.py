"""
Ввести строку. Если длина строки больше 10 символов, то создать новую
строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки
"""

string = input("Enter a string: ")
new_string = len(string)
if new_string >= 10:
    print('!!!')
else:
    print(string[1])