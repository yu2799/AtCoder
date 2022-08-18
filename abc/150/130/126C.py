from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    res = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        res += 1 / pow(2, cnt)
    print(res / n)


if __name__ == "__main__":
    main()
