from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    res = [0] * min(h, w)
    c = [list(input()[:-1]) for _ in range(h)]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if c[i][j] != "#":
                continue
            if c[i - 1][j - 1] != "#":
                continue
            if c[i - 1][j + 1] != "#":
                continue
            if c[i + 1][j - 1] != "#":
                continue
            if c[i + 1][j + 1] != "#":
                continue
            cnt = 2
            while i + cnt < h and j + cnt < w and c[i + cnt][j + cnt] == "#":
                cnt += 1
            res[cnt - 2] += 1

    print(*res)


if __name__ == "__main__":
    main()
