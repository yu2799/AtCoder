from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    grid = [list(input()[:-1]) for _ in [0] * h]
    tmp1 = [["#"] * w for _ in [0] * h]
    dir = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (0, 0),
    ]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == ".":
                for dx, dy in dir:
                    x = dx + j
                    y = dy + i
                    if 0 <= x < w and 0 <= y < h:
                        tmp1[y][x] = "."

    tmp2 = [["."] * w for _ in [0] * h]
    for i in range(h):
        for j in range(w):
            if tmp1[i][j] == "#":
                for dx, dy in dir:
                    x = dx + j
                    y = dy + i
                    if 0 <= x < w and 0 <= y < h:
                        tmp2[y][x] = "#"

    if grid == tmp2:
        print("possible")
        for i in tmp1:
            print(*i, sep="")
    else:
        print("impossible")


if __name__ == "__main__":
    main()
