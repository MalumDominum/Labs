# coding=utf-8
import numpy as np

vertical = int(input("Enter how many elements by vertical you want: "))  # Ввод изначального массива
horizontal = int(input("Enter how many elements by horizontal you want: "))
a = np.random.randint(-100, 101, size=(vertical, horizontal))
print (a)

sum_element = 0  # Сумма всех элементов массива. Эквивалентно sum_element = a.sum()
for i in range(int(vertical)):
    for g in range(int(horizontal)):
        element = a[i, g]
        sum_element += element
print ("Sum of the all elements: " + str(sum_element))

h_array = []  # Вертикальный массив суммы елементов
wanted_element = 0
for i in range(int(vertical)):
    for g in range(int(horizontal)):
        element = a[i, g]
        wanted_element += element
    h_array.append(int(wanted_element))
    wanted_element = 0
v_array = np.array(h_array)[:, np.newaxis]
print ("Vertical array:")
print (v_array)

h_array = [sum_element]  # Горизонтальный массив суммы елементов
for g in range(int(horizontal)):
    for i in range(int(vertical)):
        element = a[i, g]
        wanted_element += element
    h_array.append(int(wanted_element))
    wanted_element = 0
print ("Horizontal array: " + str(h_array))

li = [h_array]  # Добавление массивов к изначальному
a = np.concatenate((v_array, a), axis=1)
a = np.concatenate((a, li), axis=0)
print ("Wanted A(n+1, m+1):")
print (a)
