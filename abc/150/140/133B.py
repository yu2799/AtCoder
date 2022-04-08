n, d = map(int, input().split())
point = []
cnt = 0
for i in range(n):
    p = [int(i) for i in input().split()]
    point.append(p)
for i in range(n-1):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (point[i][k]-point[j][k])**2
        dist = dist**0.5
        if dist.is_integer():
            cnt += 1
print(cnt)