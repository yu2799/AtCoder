from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    if k == 0:
        print(n * n)
        return

    res = 0
    for b in range(k + 1, n + 1):
        tmp = (n + 1) // b
        d = 0

        d += (b - k) * tmp

        left = k + b * tmp
        right = n
        if left <= right:
            d += right - left + 1
        res += d
    print(res)


if __name__ == "__main__":
    main()
