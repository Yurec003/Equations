
import math

print("Input a, b, c")

a = int(input())
b = int(input())
c = int(input())

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = round((b * (-1) + math.sqrt(d)) / (2 * a))
    x2 = round((b * (-1) - math.sqrt(d)) / (2 * a))
    print("x1 =", x1, "\nx2 =", x2)
elif d == 0:
    x = round((b * (-1) + math.sqrt(d)) / (2 * a))
    print("x =", x)
else:
    print("No answers")
