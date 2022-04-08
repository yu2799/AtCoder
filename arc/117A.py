a, b = map(int, input().split())
res = []
tmp = 0
if a <= b:
    for i in range(1, a):
        res.append(i)
        res.append(-i)
    for i in range(a, b+1):
        res.append(-i)
        tmp += i
    res.append(tmp)
else:
    for i in range(1, b):
        res.append(i)
        res.append(-i)
    for i in range(b, a+1):
        res.append(i)
        tmp += i
    res.append(-tmp)
print(" ".join(str(n) for n in res))