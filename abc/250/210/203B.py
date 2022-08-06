from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    res = 0
    for i in range(1, n + 1):
        for k in range(1, k + 1):
            res = res + i * 100 + k
    print(res)


if __name__ == "__main__":
    main()
