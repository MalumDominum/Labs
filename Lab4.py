a = int(input("Enter your a: "))
b = int(input("Enter your b: "))
total_sum = 0
for i in range(a, b+1):
    if (i % 2) != 0:
        square_i = i ** 2
        print ("Answer of iteration " + str(i) + " is:" + str(square_i))
        total_sum += square_i
print ("Sum is:" + str(total_sum))
