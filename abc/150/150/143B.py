n = int(input())
d = [int(i) for i in input().split()]
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        res += d[i] * d[j]
print(res)