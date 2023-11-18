from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    set_c = [set() for _ in range(n)]
    for i in range(n):
        set_c[i].add(c[i])

    res = []
    for _ in range(q):
        i, j = map(lambda x: int(x) - 1, input().split())
        if len(set_c[i]) < len(set_c[j]):
            set_c[j] |= set_c[i]
            set_c[i].clear()
        else:
            set_c[i] |= set_c[j]
            set_c[j].clear()
            set_c[i], set_c[j] = set_c[j], set_c[i]
        res.append(len(set_c[j]))
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
