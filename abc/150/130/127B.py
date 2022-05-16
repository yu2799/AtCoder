from sys import stdin


def main():
    input = stdin.readline
    r, d, x = map(int, input().split())
    res = []
    for _ in [0] * 10:
        x = r * x - d
        res.append(x)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
