h, w = map(int, input().split())
grid = ["." * (w + 2)] + ["." + input() +
                          "." for _ in [0] * h] + ["." * (w + 2)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(1, h+1):
    for j in range(1, w+1):
        if grid[i][j] == "#":
            for x, y in zip(dx, dy):
                if grid[i+y][j+x] == "#":
                    break
            else:
                print("No")
                exit()
print("Yes")
