import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
n = int(input())
res = 2
for i in range(3, n+1):
    res = lcm(res, i)
print(res+1)