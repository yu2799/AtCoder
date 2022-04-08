from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = [i for i in map(int, input().split())]
    res = 0
    tmp = 0
    r = 0
    for l in range(n):
        while r < n and tmp < k:
            tmp += a[r]
            r += 1
        if tmp >= k:
            res += n - r + 1
        tmp -= a[l]
    print(res)


if __name__ == "__main__":
    main()
