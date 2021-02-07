"""
найти все слова в строке где больше 7 символов
"""
string = 'String will never be empty and you do not need to account for different data types and string that not ' \
         'stupid data type in python. That string.'.split()
result = [i for i in string if len(i) > 7]
print(result)