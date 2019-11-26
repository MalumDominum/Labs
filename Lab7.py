# coding=utf-8

num_array_A = list()
NUM = int(input("Enter how many elements you want: "))
print ("Enter numbers in array A(n): ")  # Ввод массива A(n)
for i in range(int(NUM)):
    n_A = input("Num " + str(i + 1) + ": ")
    num_array_A.append(int(n_A))
print ("Array A(n): " + str(num_array_A))

num_array_B = list()
print ("Enter numbers in array B(n): ")  # Ввод массива B(n)
for i in range(int(NUM)):
    n_B = input("Num " + str(i + 1) + ": ")
    num_array_B.append(int(n_B))
print ("Array B(n): " + str(num_array_B))

max_A_B = max(max(num_array_A), max(num_array_B))  # Максимальный элемент из двух массивов
print ("Maximum element in arrays A(n) and B(n): " + str(max_A_B))


def gcd(a, b):  # Функция Алгоритма Евклида(Найбольший общий делитель)
    while b != 0:
        a, b = b, a % b
    print("Greatest common divisor: " + str(a))
    return a


num_array_C = list()

for i in range(int(NUM)):       # Определение и вывод C(n) используя Алгоритм Евклида
    element_A = num_array_A[i]  # и умножение всех элементов на максимальный элемент массивов
    element_B = num_array_B[i]
    num_array_C.append(int(gcd(element_A, element_B) * max_A_B))
print ("Array C(n): " + str(num_array_C))
