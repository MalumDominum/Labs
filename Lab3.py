import math

x = float(input("Enter your x: "))
if x > 4 or x < 0:
    print ("You input wrong x")
    quit(1)
n = 0
numerator = (-1) ** n * (x ** (2 * n))
denominator = math.factorial(2 * n)
s = numerator/denominator
total = 0
while math.fabs(s) > 1e-5:
    numerator = (-1) ** n * (x ** (2 * n))
    # print ("Numerator is: " + str(numerator))
    denominator = math.factorial(2 * n)
    # print ("Denominator is: " + str(denominator))
    s = numerator / denominator
    print ("Answer of iteration " + str(n) + " is:" + str(s))
    n += 1
    total += s
# print ("Sum is:" + str(total))
print ("Rounded sum is:" + str(round(total, 4)))
