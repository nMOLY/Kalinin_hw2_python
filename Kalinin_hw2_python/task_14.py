# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N: "))
i = 1
while i <= N:
    print(i)
    i *= 2
    