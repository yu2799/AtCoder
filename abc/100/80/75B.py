h, w = map(int, input().split())
grid = ["." * (w + 2)] + ["." + input() +
                          "." for _ in [0] * h] + ["." * (w + 2)]
res = [[0 for _ in [0] * w] for _ in [0] * h]
dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

for i in range(1, h+1):
    for j in range(1, w+1):
        cnt = 0
        if grid[i][j] == ".":
            for x, y in zip(dx, dy):
                if grid[i+y][j+x] == "#":
                    cnt += 1
            res[i-1][j-1] = str(cnt)
        else:
            res[i-1][j-1] = "#"

for i in range(h):
    print(*res[i], sep="")
