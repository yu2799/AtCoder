from math import gcd
a, b, c, d = map(int, input().split())
l = c*d//gcd(c, d)
print((b - (b//c + b//d) + b//l) - ((a-1) - ((a-1)//c + (a-1)//d) + (a-1)//l))