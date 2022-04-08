n = int(input())
w = [int(i) for i in input().split()]
res = 10**10
for i in range(1, n):
    res = min(res, abs(sum(w[:i]) - sum(w[i:])))
print(res)