# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4


import os
def clear_console():
    os.system("cls")
clear_console()

a = int(input("Число а: "))
b = int(input("Число б: "))

def sum(a,b):
    if a == 0:
          return b
    if b == 0:
          return a
    else:
          return sum(a-1,b+1)
print(sum(a,b))
