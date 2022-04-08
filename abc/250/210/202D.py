from math import factorial

a, b, k = map(int, input().split())
res = []
tmp = 0
i = 1
while a != 0 and b != 0:
    tmp = factorial(a + b - 1) // factorial(a - 1) // factorial(b)
    if tmp >= k:
        res.append("a")
        a -= 1
    else:
        res.append("b")
        k -= factorial(a + b - 1) // factorial(a - 1) // factorial(b)
        b -= 1
    i += 1

if a == 0:
    for _ in range(b):
        res.append("b")
elif b == 0:
    for _ in range(a):
        res.append("a")

print("".join(res))
