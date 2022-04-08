from math import pi, cos, sqrt

a, b, h, m = map(int, input().split())
s = (h + m / 60) / 6 * pi
l = m / 30 * pi
print(sqrt(a*a + b*b - 2*a*b*cos(abs(l-s))))
