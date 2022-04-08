n = int(input())
b = [int(i) for i in input().split()]
res = b[0]
for i in range(1, n-1):
    res += min(b[i-1], b[i])
print(res+b[n-2])