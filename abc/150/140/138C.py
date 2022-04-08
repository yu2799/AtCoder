n = int(input())
v = sorted([int(i) for i in input().split()])
res = v[0]
for i in range(1, n):
    res = (res+v[i])/2
print(v.pop())