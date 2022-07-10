from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    cd = [tuple(map(int, input().split())) for _ in [0] * m]
    res = []
    for a, b in ab:
        tmp_min = 4 * 10**8 + 1
        point = 0
        for idx, (c, d) in enumerate(cd):
            tmp = abs(a - c) + abs(b - d)
            if tmp < tmp_min:
                tmp_min = tmp
                point = idx
        res.append(point + 1)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
