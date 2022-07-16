from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = (
        [list("." * (w + 2))]
        + [list("." + input()[:-1] + ".") for _ in [0] * h]
        + [list("." * (w + 2))]
    )
    dir = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    res = [[] for _ in [0] * h]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if s[i][j] == ".":
                tmp = 0
                for x, y in dir:
                    if s[i + y][j + x] == "#":
                        tmp = tmp + 1
                res[i - 1].append(tmp)
            else:
                res[i - 1].append("#")
    for i in res:
        print(*i, sep="")


if __name__ == "__main__":
    main()
