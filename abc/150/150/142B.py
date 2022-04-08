n, k = map(int, input().split())
h = [int(i) for i in input().split()]
res = 0
for i in h:
    if i >= k:
        res += 1
print(res)