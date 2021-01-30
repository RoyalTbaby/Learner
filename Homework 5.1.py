"""
Написать программу, в которой вводятся два операнда Х и Y и знак
операции sign (+, –, /, *). Вычислить результат Z в зависимости от знака.
Предусмотреть реакции на возможный неверный знак операции, а также на ввод Y=0
при делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл).
В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').
"""

while True:
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    sign = input("Enter sign (+, -, *, /) ")
    if sign == "+":
        z = x + y
    elif sign == "-":
        z = x - y
    elif sign == "*":
        z = x * y
    elif sign == "/":
        if y == 0:
            print("The division by 0 is invalid")
            continue
        z = x / y
    elif sign == 0:
        print("Finish - you're done!")
        break
    else:
        print("Invalid action")
        continue

    print(f'The result is {z}')