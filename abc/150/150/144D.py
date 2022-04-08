from math import degrees, atan
a, b, x = map(int, input().split())
s = x / a
if (a*b) / 2 > s:
    y = s * 2 / b
    print(degrees(atan(b/y)))
else:
    y = (a*b-s) * 2 / a
    print(degrees(atan(y/a)))
