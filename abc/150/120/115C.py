from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    h = [int(input()) for _ in [0] * n]
    h.sort()
    res = h[k - 1] - h[0]
    for i in range(1, n - k + 1):
        tmp = h[i + k - 1] - h[i]
        if tmp < res:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
