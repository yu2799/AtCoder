from sys import stdin


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    res = [list("." * (s - r + 1)) for _ in [0] * (q - p + 1)]
    k1 = max(p - a, r - b)
    k2 = min(q - a, s - b)
    for i in range(k1, k2 + 1):
        res[a + i - p][b + i - r] = "#"

    k3 = max(p - a, b - s)
    k4 = min(q - a, b - r)
    for i in range(k3, k4 + 1):
        res[a + i - p][b - i - r] = "#"
    for i in res:
        print(*i, sep="")


if __name__ == "__main__":
    main()
