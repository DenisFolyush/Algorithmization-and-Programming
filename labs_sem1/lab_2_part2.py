import math
h = 0.2
a = 5
b = 8
x = 5
while a <= x < b:
    if x < 6:
        F1 = 1 / (1 - math.log(x + 1))
        print("x=", round(x,3), F1)
    elif 6 <= x < 7:
        F2 = math.sin(math.cos(x))
        print("x=", round(x, 3), F2)
    elif x >= 8:
        F3 = math.log(math.pow(math.e, x) + math.pow(x,2))
        print("x=", round(x, 3), F3)
    x += h
