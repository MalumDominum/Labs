import math

a = float(input("Enter your a: "))
b = float(input("Enter your b: "))
c = float(input("Enter your c: "))
d = float(input("Enter your d: "))


def f(x, y):
    return x ** 2 - y ** 2


def g(x, y, z):
    return (x + y) / (4 * z * x)


first_member = (f(a, b) + f(c, d)) / (math.sqrt(g(a, b, c)))
second_member = (c - g(a, b, c) + 1) / (f(b, c) - f(a, b))
third_member = 1 + (math.sqrt(g(a, b, c)) / (f(b, c) - f(a, c)))
y = first_member + second_member * third_member
print("First member is:" + str(first_member))
print("Second member is:" + str(second_member))
print("Third member is:" + str(third_member))
print("Final answer is:" + str(y))
