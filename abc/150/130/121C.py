from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    ab.sort()
    res = 0
    for a, b in ab:
        if m - b > 0:
            res += a * b
            m -= b
        else:
            res += a * m
            print(res)
            return


if __name__ == "__main__":
    main()
