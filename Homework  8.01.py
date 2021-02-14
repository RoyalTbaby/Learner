"""
Дан список слов. Сгенерировать новый список с перевернутыми словами
"""
list = ['baby', 'child', 'teen', 'adult', 'elderly']
new_list = [i for i in list[::-1]]
print(new_list)