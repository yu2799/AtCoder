h, w = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(h)]
row = [0] * h
col = [0] * w
for i in range(h):
    for j in range(w):
        row[i] += a[i][j]
        col[j] += a[i][j]

for i in range(h):
    for j in range(w):
        print(row[i] + col[j] - a[i][j], end=" ")
    print("")
