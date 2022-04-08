from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    csf = [[i for i in map(int, input().split())] for _ in [0] * (n - 1)]
    res = []
    for i in range(n):
        t = 0
        for j in range(i, n - 1):
            c, s, f = csf[j]
            if t < s:
                t = s
            elif t % f:
                t += f - t % f
            t += c
        res.append(t)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
