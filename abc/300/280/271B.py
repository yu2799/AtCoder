from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    l = []
    for _ in [0] * n:
        _, *a = map(int, input().split())
        l.append(list(a))
    res = []
    for _ in [0] * q:
        s, t = map(lambda x: int(x) - 1, input().split())
        res.append(l[s][t])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
