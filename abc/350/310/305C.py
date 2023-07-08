from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    grid = (
        [list("." * (w + 2))]
        + [list(".") + list(input()[:-1]) + list(".") for _ in [0] * h]
        + [list("." * (w + 2))]
    )
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i][j] == "#":
                continue
            cnt = 0
            for x, y in dir:
                if grid[y + i][x + j] == "#":
                    cnt += 1
            if cnt >= 2:
                print(i, j)
                return


if __name__ == "__main__":
    main()
