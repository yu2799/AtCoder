from sys import stdin


def main():
    input = stdin.readline
    n, m, t = map(int, input().split())
    res = n
    tmp = 0
    for _ in [0] * m:
        a, b = map(int, input().split())
        res -= a - tmp
        if res <= 0:
            print("No")
            return
        res += b - a
        if res > n:
            res = n
        tmp = b
    print("Yes" if t - tmp < res else "No")


if __name__ == "__main__":
    main()
