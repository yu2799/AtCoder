from sys import stdin


def main():
    input = stdin.readline
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    res = k + a[0] - a[-1]
    for i in range(n - 1):
        tmp = a[i + 1] - a[i]
        if res < tmp:
            res = tmp
    print(k - res)


if __name__ == "__main__":
    main()
