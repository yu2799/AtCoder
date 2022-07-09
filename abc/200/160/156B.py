from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    tmp = 1
    res = 0
    while tmp <= n:
        res += 1
        tmp *= k
    print(res)


if __name__ == "__main__":
    main()
