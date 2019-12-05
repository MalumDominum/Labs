# coding=utf-8
import numpy as np


def sum_element(a, sum_element=0):  # Сумма всех элементов массива. Эквивалентно sum_element = a.sum()
    for i in range(int(vertical)):
        for g in range(int(horizontal)):
            element = a[i, g]
            sum_element += element
    return sum_element


def sum_array_vertical(a, array, wanted_element = 0):
    for i in range(int(vertical)):
        for g in range(int(horizontal)):
            element = a[i, g]
            wanted_element += element
        array.append(int(wanted_element))
        wanted_element = 0

def sum_array_horizontal(a, array, wanted_element = 0):
    for g in range(int(horizontal)):
        for i in range(int(vertical)):
            element = a[i, g]
            wanted_element += element
        array.append(int(wanted_element))
        wanted_element = 0

vertical = int(input("Enter how many elements by vertical you want: "))  # Ввод изначального массива
horizontal = int(input("Enter how many elements by horizontal you want: "))
a = np.random.randint(-100, 101, size=(vertical, horizontal))
print (a)

sum_element = sum_element(a)

h_array = []  # Вертикальный массив суммы елементов

sum_array_vertical(a, h_array)

print ("Horizontal array: " + str(h_array))

li = [h_array]  # Добавление массивов к изначальному
a = np.concatenate((v_array, a), axis=1)
a = np.concatenate((a, li), axis=0)
print ("Wanted A(n+1, m+1):")
print (a)
