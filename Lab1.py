import math

a = float(input("Enter your first side: "))
b = float(input("Enter your second side: "))
angle_degree = float(input("Enter angle between sides: "))
if angle_degree >= 180 or angle_degree <= 0:
    print ("You input wrong angle")
    quit(1)
angle_radian = angle_degree * math.pi / 180
answer = math.cos(angle_radian)
c = math.sqrt(a ** 2 + b ** 2 - a * b * 2 * answer)
if all([a + b > c, b + c > a, c + a > b]):
    print("Triangle exists")
else:
    print ("Triangle not exists")
    quit(1)
print ("Angle in Radians: " + str(angle_radian))
print ("Cosine: " + str(answer))
print ("Final Answer: " + str(c))
