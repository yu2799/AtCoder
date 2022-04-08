from math import gcd

a, b, c = map(int, input().split())
tmp = gcd(a, gcd(b, c))
print((a+b+c)//tmp - 3)
