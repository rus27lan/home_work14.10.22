# Задачи:
# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# from curses.ascii import isdigit

# number = int(input("Сколько чисел будет в списке: "))
# print("Введите по очереди числа что бы добавить их в список: ")
# list = []
# i = 0
# while int(i) < number:
#     numbers = input()
#     list.append(numbers)
#     i += 1
# print(list)

# count = 1
# sum = 0
# while count < number:
#     sum = sum + int(list[count])
#     count += 2
# print(f"ответ: {sum}")



# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]


# number = int(input("Сколько чисел будет в списке: "))
# print("Введите по очереди числа что бы добавить их в список: ")
# list = []
# i = 0
# while int(i) < number:
#     numbers = input()
#     list.append(numbers)
#     i += 1
# print(list)

# count = 1
# list2 = []
# element = 0
# while count < number/2 + 1:
#     element = int(list[count-1]) * int(list[number - count])
#     list2.append(element)
#     count += 1
# print(list2)


# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# number = float(input("Сколько чисел будет в списке: "))
# print("Введите по очереди числа что бы добавить их в список: ")
# list = []
# i = 0
# while int(i) < number:
#     numbers = input()
#     list.append(numbers)
#     i += 1
# print(list)

# list2 = []
# count = 0
# element = 0
# while count < number:
#     element = float(list[count]) % 1
#     list2.append(element)
#     count += 1
# answer = max(list2) - min(list2)
# print(answer)

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

# import numbers


# number = int(input("Введите десячичное число: "))
# # print(bin(number)) 
# # print(format(number, "b"))
# # Решение с помощью функций
# answer = ''
# while number > 0:
#     answer = str(number % 2) + answer
#     number = number // 2
# print(answer)

# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]


number = int (input("Введите число: "))
def Fibonachi(number):
    if number in (1,2):
        return 1
    return Fibonachi( number - 1 ) + Fibonachi ( number - 2 )
def notFibonachi(number):
    if number in (1,2):
        return 1
    return notFibonachi( number + 2 ) - notFibonachi ( number + 1 )
list = []
for i in range(- number, 1):
    list.append(notFibonachi(i))
for i in range(1, number + 1):
    list.append(Fibonachi(i))
print(list)




# git remote add origin https://github.com/rus27lan/home_work14.10.22.git
# git branch -M main
# git push -u origin main

