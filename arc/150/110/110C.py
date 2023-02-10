from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    res = []
    prev = 1
    ok = 0
    for i in range(n):
        if p[i] == i + 1:
            print(-1)
            return
        if p[i] == prev:
            for j in range(i, ok, -1):
                p[j], p[j - 1] = p[j - 1], p[j]
                res.append(j)
            ok = i
            prev = i + 1
    for i in range(n):
        if p[i] != i + 1:
            print(-1)
            return
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
