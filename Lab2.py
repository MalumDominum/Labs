x = float(input("Enter your x: "))
y = float(input("Enter your y: "))
if all([x <= 0, y >= 1 - x]) or all([x >= 1, y >= 1 - x]):
    print ("Dot's in the area")
else:
    print ("Dot's not in the area")
