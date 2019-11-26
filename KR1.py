import math

x = float(input("Enter your x: "))
if x == 1:
    print ("You input wrong x")
    quit(1)
n = int(input("Enter your n: "))
numerator = math.atan(x)
denominator = (x - 1) ** n
s = numerator/denominator
total = 0
for i in range(n):
    numerator = math.atan(x)
    # print ("Numerator is: " + str(numerator))
    denominator = (x - 1) ** i
    # print ("Denominator is: " + str(denominator))
    s = numerator / denominator
    print ("Answer of iteration " + str(i) + " is:" + str(s))
    total += s
# print ("Sum is:" + str(total))
print ("Rounded sum is:" + str(round(total, 4)))
