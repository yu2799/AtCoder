from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    res = []
    d = set()
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            d.add((a, b))
        elif t == 2:
            if (a, b) in d:
                d.remove((a, b))
        else:
            if (a, b) in d and (b, a) in d:
                res.append("Yes")
            else:
                res.append("No")
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
