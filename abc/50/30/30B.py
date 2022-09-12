from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    if n >= 12:
        n -= 12
    res = abs(30 * n + 30 * (m / 60) - 6 * m)
    print(360 - res if res > 180 else res)


if __name__ == "__main__":
    main()
