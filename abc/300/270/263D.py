from sys import stdin


def main():
    input = stdin.readline
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    res = r * n
    tmp = 0
    for i in range(n):
        tmp = min(tmp + a[i], l * (i + 1))
        res = min(res, tmp + r * (n - 1 - i))
    print(res)


if __name__ == "__main__":
    main()
