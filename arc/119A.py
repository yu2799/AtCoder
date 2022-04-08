n = int(input())
b = 0
tmp = 1
res = 10**18
while tmp <= n:
    a = n // (2 ** b)
    c = n % (2 ** b)
    res = min(res, a + b + c)
    tmp *= 2
    b += 1
print(res)
