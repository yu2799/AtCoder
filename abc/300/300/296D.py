from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    res = float("inf")
    for i in range(1, n + 1):
        tmp = (m + i - 1) // i
        if tmp <= n:
            res = min(res, tmp * i)
        if tmp < i:
            break
    print(res if res != float("inf") else -1)


if __name__ == "__main__":
    main()
